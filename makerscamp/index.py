from xmlrpc.client import Boolean
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from makerscamp.db import DB
from makerscamp.classes.user import User

bp = Blueprint('index', __name__)

@bp.route('/')
def home():
    #result= DB.exec("SELECT * FROM users")
    #print(result)
    #DB.exec("INSERT INTO channels(name) VALUES('testing32411342')")
    #result3 = DB.exec("SELECT * FROM channels")
    #print(result3)
    print("on index")
    return render_template('home.html')


@bp.route('/jonahtest')
def jonah_test():
    print("hi")
    return redirect(url_for("index.home"))

@bp.route('/test_users')
def test_users():
    result= DB.exec("SELECT * FROM users")
    print(result)

    #User.create("John")

    return render_template('home.html')


