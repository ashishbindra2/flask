from flask import Flask,session,redirect,render_template,jsonify,request,flash,url_for
from db import get_comapny,get_job
from helper import data,insert_scraped_data
app = Flask(__name__)

app.secret_key = "fake_key"

@app.get("/")
def test():
    companies = get_comapny()
    return render_template('index.html',companies=companies)

@app.get("/jobs")
def jobs():
    jobs = get_job()
    
    return render_template('jobs.html',jobs=jobs)

@app.get("/insert")
def index():
    insert_scraped_data(data, 'JobAt')
    return redirect(url_for('test'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7007)
