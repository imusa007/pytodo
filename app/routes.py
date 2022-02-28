from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import Todo
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    """todo_list=[
        {
        "id":1,
        "title":"Hello"
        },
        {
            "id": 2,
            "title": "world"
        },

        ]
        """
    todo_list = Todo.query.all()
    return render_template('base.html', title='Test is ok', todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    title=request.form.get('title')
    todo=Todo(title=title,time_added=datetime.utcnow(),complete=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo=Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))