from xmlrpc.client import Boolean
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from makerscamp.db import DB


bp = Blueprint('index', __name__)

@bp.route('/')
def home():
    result= DB.exec("SELECT * FROM users")
    print(result)

    DB.exec("INSERT INTO channels(name) VALUES('testing32411342')")

    result3 = DB.exec("SELECT * FROM channels")
    print(result3)

    return render_template('home.html')
