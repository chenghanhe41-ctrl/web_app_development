from flask import Blueprint, render_template, request, redirect, url_for
from app.models.task import (
    get_all_tasks,
    get_task_by_id,
    create_task as create_task_model,
    update_task,
    delete_task_by_id,
    toggle_task_status
)

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/')
def index():
    status = request.args.get('status')
    tasks = get_all_tasks(status)
    return render_template('index.html', tasks=tasks, status=status)

@task_bp.route('/tasks/new', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')

        if title:
            create_task_model(title, description)

        return redirect(url_for('tasks.index'))

    return render_template('create_task.html')

@task_bp.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = get_task_by_id(task_id)

    if not task:
        return redirect(url_for('tasks.index'))

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')

        if title:
            update_task(task_id, title, description)

        return redirect(url_for('tasks.index'))

    return render_template('edit_task.html', task=task)

@task_bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    delete_task_by_id(task_id)
    return redirect(url_for('tasks.index'))

@task_bp.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    toggle_task_status(task_id)
    return redirect(url_for('tasks.index'))
