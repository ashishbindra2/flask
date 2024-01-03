from flask import render_template, redirect, url_for
from app.admin import admin_bp
from flask_login import login_required, current_user, logout_user


@admin_bp.route('/')
@login_required
def admin_index():
    return render_template('admin/index.html', name=current_user.name)


@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
