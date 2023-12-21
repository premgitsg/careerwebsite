from flask import Flask, render_template, jsonify 
app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'RS. 10,00,000'
  },
  {
    'id':2,
    'title':'Business Analyst',
    'location':'Bengaluru, India',
    'salary':'RS. 10,00,000'
  },
  {
  'id':3,
  'title':'Data Engineer',
  'location':'Chennai, India',
  'salary': ''
  },
  {
  'id':4,
  'title':'Backend Engineer',
  'location':'Bengaluru, India',
  'salary':'USD. 1000'
  }
]
@app.route("/")
def hello_world():
  return render_template(
    "home.html", jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)