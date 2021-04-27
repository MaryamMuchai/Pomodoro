from flask import render_template ,request,redirect
from . import auth

@auth.route('/login')
def login():
    return
    render_template('auth/login.html')

