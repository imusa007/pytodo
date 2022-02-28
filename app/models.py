from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    time_added=db.Column(db.DateTime)
    complete = db.Column(db.Boolean)