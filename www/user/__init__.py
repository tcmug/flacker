# USER

from flask import Blueprint, abort

user = Blueprint('user', __name__, template_folder='templates')

from views import *
