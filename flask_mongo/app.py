from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MONGO_URI'] = 'mongodb+srv://blueaves15:test15@blueaves.dha4hvq.mongodb.net/?retryWrites=true&w=majority'

mongo = PyMongo(app)

login_manager = LoginManager(app)

login_manager.login_view = 'login'


class User(UserMixin):
    pass

# Example usage
@app.route('/')
def index():
    users_collection = mongo.db.users
    # Now you can perform operations on the users collection
    return 'Hello, MongoDB!'

@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({'_id': user_id})
    if user_data:
        user = User()
        user.id = user_id
        return user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_data = mongo.db.users.find_one({'username': username})
        if user_data and check_password_hash(user_data['password'], password):
            user = User()
            user.id = str(user_data['_id'])
            login_user(user)
            return redirect(url_for('dashboard'))

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = mongo.db.users.find_one({'username': username})

        if existing_user:
            return 'Username already exists! Please choose a different one.'

        hashed_password = generate_password_hash(password, method='sha256')
        user_id = mongo.db.users.insert({'username': username, 'password': hashed_password})

        user = User()
        user.id = str(user_id)
        login_user(user)

        return redirect(url_for('dashboard'))

    return render_template('register.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello, {current_user.id}! You are logged in.'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
