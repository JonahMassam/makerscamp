from xmlrpc.client import Boolean
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from makerscamp.db import get_db


bp = Blueprint('index', __name__)

@bp.route('/')
def home():
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM users')
    result = cur.fetchall()

    print(result)

    return render_template('home.html')
