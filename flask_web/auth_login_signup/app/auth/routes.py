from flask import render_template, request, url_for, flash, redirect
from flask_login import login_required, logout_user,login_user

from app.auth import auth_bp
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import User
from app.extensions import db


@auth_bp.route('/')
# @auth_bp.route('/login')
def login():
    return render_template('auth/login.html')


@auth_bp.route('/', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    print(email, password)
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        print('error')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page
    print("longed in")
    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('admin.admin_index'))


@auth_bp.route('/signup')
def signup():
    return render_template('auth/register.html')


@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    repass = request.form.get('repass')

    user = User.query.filter_by(
        email=email).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    if password != repass:
        flash('Password does not match!!')
        return redirect(url_for('auth.signup'))
    hashed_password = generate_password_hash(password)

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=hashed_password)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_bp.route('/print_users')
def print_users():
    # Retrieve all users from the database
    all_users = User.query.all()

    # Print the users (for demonstration purposes)
    for user in all_users:
        print(f'User ID: {user.id}, Email: {user.email}, Name: {user.name}, Password: {user.password}')

    # Alternatively, you can pass the users to a template and render it in the browser
    return render_template('print_users.html', users=all_users)
