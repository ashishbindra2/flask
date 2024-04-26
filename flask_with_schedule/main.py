from flask import Flask,render_template
from util import log_cpu_usage, log_ram_usage, print_message
from flask_apscheduler import APScheduler

app = Flask(__name__,template_folder='templates')

schedular = APScheduler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/other")
def other():
    schedular.remove_job('messagejob')
    return render_template('other.html')

if __name__ == '__main__':
    schedular.add_job(func=log_cpu_usage, trigger = 'interval', seconds=5, id='cpujob')
    schedular.add_job(func=log_ram_usage, trigger = 'interval', seconds=10, id='ramjob')
    schedular.add_job(func=print_message, args=('My Message',), trigger = 'interval', seconds=2, id='messagejob')
    schedular.start()
    app.run(debug=False,host='0.0.0.0')