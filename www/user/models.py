

from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp
from wtforms.widgets import TextArea
from flask_login import UserMixin


from main import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self):
        #self.username = username
        #self.email = email
        self.name = ""

    def __repr__(self):
        return '<User %r>' % self.username



class LoginForm(Form):
    name = StringField('Name',
        validators=[
            DataRequired(),
            Regexp('^\w+$', message="Username must contain only letters numbers or underscore"),
        ]
    )
    password = PasswordField('Password')
    submit = SubmitField('Log in')

