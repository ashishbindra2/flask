import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

# ... psycopg2 library so that you can interact with your database using Python.

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            # user=os.environ['DB_USERNAME'], import the os module you’ll use to access environment variables where you’ll store your database username and password so that they are not visible in your source code.
                            # password=os.environ['DB_PASSWORD']     export DB_USERNAME="sammy"
                                                                        # export DB_PASSWORD="password" in cmd


                            user = 'postgres',
                            password = 'ROOT'
                            )
    return conn

# ...


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)