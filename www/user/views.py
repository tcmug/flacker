
from flask import request, redirect, url_for, render_template, flash, abort
from flask_login import login_required, LoginManager, UserMixin, login_user, logout_user

from main import app
from __init__ import user
from models import User

# Inject login manager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    from user import User
    return User()


@login_manager.unauthorized_handler
def unauthorized_callback():
    """Unauthorized callbacks bounce to login"""
    return redirect(url_for('user.user_login'))


@user.route('/login', methods=["GET", "POST"])
def user_login():
    """Present the login form on GET and handle login on POST"""
    from models import LoginForm

    form = LoginForm()

    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        if user.password == 'hello':
            login_user(user, remember = True)
            return redirect(url_for('index'))

    return render_template('pages/login.html', login_form = form)


@user.route('/reset/<token>', methods=["GET", "POST"])
def user_reset(token):

    from models import User

    user = User.query.filter_by(login_token=token).first()
    if not user:
        abort(404, 'nope')

    login_user(user, remember = True)

    # Clear login token.
    user.login_token = None
    from main import db
    db.session.commit()

    return redirect(url_for('index'))


@login_required
@user.route('/password', methods=["GET", "POST"])
def user_password():
    """Present the login form on GET and handle login on POST"""
    from models import PasswordChangeForm

    form = PasswordChangeForm()

    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        if user.password == 'hello':
            login_user(user, remember = True)
            return redirect(url_for('index'))

    return render_template('pages/login.html', login_form = form)



@user.route('/logout', methods=["GET", "POST"])
@login_required
def user_logout():
    """Logout user and bounce to the login page"""
    logout_user()
    return redirect(url_for('user.user_login'))

