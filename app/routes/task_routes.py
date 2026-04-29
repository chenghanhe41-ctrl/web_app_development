from flask import Blueprint, render_template, request, redirect, url_for

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/')
def index():
    return render_template('index.html')

@task_bp.route('/tasks/new', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        return redirect(url_for('tasks.index'))
    return render_template('create_task.html')

@task_bp.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        return redirect(url_for('tasks.index'))
    return render_template('edit_task.html')

@task_bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    return redirect(url_for('tasks.index'))

@task_bp.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    return redirect(url_for('tasks.index'))
