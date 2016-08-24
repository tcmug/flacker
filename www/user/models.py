
from werkzeug.security import generate_password_hash, \
     check_password_hash

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
    password_hash = db.Column(db.String(160), unique=False)
    login_token = db.Column(db.String(160), unique=False)

    def __init__(self):
        self.id = None
        self.username = None
        self.email = None
        self.password_hash = None
        self.login_token = None

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_one_time_login_url(self):
        return "user/reset/" + self.login_token
        #return url_for('user.reset', token=self.login_token)


class PasswordChangeForm(Form):
    password = PasswordField('Password')
    submit = SubmitField('Submit password change')


class LoginForm(Form):
    name = StringField('Name',
        validators=[
            DataRequired(),
            Regexp('^\w+$', message="Username must contain only letters numbers or underscore"),
        ]
    )
    password = PasswordField('Password')
    submit = SubmitField('Log in')



