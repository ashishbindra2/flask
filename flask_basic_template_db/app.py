from flask import Flask,session,redirect,render_template,jsonify,request,flash,url_for
from db import mangas_list,update_manga_detail,get_manga_by_id

app = Flask(__name__)

app.secret_key = "fake_key"

@app.get("/")
def test():
    return "hi there"

@app.get("/get_mangas")
def index():
    return render_template('index.html', )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7007)
