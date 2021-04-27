from flask import render_template ,request,redirect, url_for
from . import auth
from .forms import RegistrationForm
from .models import User
from ..import db

@auth.route('/login')
def login():
    return
    render_template('auth/login.html')

@auth