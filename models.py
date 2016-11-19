from connect import *
from sqlalchemy.orm import relationship
from slugify import slugify
from wtforms.widgets import * #TextArea
from wtforms import * #TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField,validators, ValidationError
import wtforms.widgets.core

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email= db.Column(db.String(50),nullable=True)
    published_at=db.Column(db.TIMESTAMP,server_default=db.func.current_timestamp())
    def __init__(self, username, email):
        self.username = username
        self.email=email
    def add(data):
        db.session.add(data)
        return db.session.commit()
    def update(self):
        return session_commit()
    def delete(var1):
        db.session.delete(var1)
        return session_commit()
if __name__ == '__main__':
    app.secret_key = SECRET_KEY
    app.config['DEBUG'] = True
    # app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    manager.run()
    app.run()


