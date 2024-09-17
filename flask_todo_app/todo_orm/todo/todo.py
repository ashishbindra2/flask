from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from todo.auth import login_required
from todo.db import get_db

bp = Blueprint('todo', __name__)


@bp.route('/')
def index():
    db = get_db()
    todo = db.execute(
        'SELECT t.id, name, created, status, priority, task_id, username'
        ' FROM task t JOIN user u ON t.task_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    
    return render_template('task/index.html', todo=todo)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('name')
        status = request.form.get('status')
        priority = request.form.get('priority')
        error = None

        print(title)
        print(status)
        print(priority)
        if not title:
            error = 'Title is required.'

        if not status:
            error = "Status is required"
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO task (name, status,priority, task_id)'
                ' VALUES (?, ?, ?, ?)',
                (title, status, priority, g.user['id'])
            )
            db.commit()
            return redirect(url_for('todo.index'))

    return render_template('task/create.html')


def get_post(id, check_author=True):
    task = get_db().execute(
        'SELECT t.id, name, status, priority, created, task_id, username'
        ' FROM task t JOIN user u ON t.task_id = u.id'
        ' WHERE t.id = ?',
        (id,)
    ).fetchone()

    if task is None:
        abort(404, f"Task id {id} doesn't exist.")

    if check_author and task['task_id'] != g.user['id']:
        abort(403)

    return task


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    task = get_post(id)

    if request.method == 'POST':
        title = request.form.get('name')
        status = request.form.get('status')
        priority = request.form.get('priority')
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE task SET name = ?, status = ?,priority = ? '
                ' WHERE id = ?',
                (title, status,priority, id)
            )
            db.commit()
            return redirect(url_for('todo.index'))

    return render_template('task/update.html', task=task)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM task WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('todo.index'))
