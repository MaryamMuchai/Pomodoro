from . import main
from flask import render_template,request,redirect
from flask_login import login_required


@main.route('/')
def index():
    title ='Pomodoro'
    message = 'Testing'
    return render_template('index.html',title=title , message=message)

