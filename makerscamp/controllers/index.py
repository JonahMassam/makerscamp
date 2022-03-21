from xmlrpc.client import Boolean
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from makerscamp.classes.db import DB
from makerscamp.classes.user import User
from makerscamp.controllers.auth import login_required
from makerscamp.classes.channel import Channel
from makerscamp.classes.message import Message

bp = Blueprint('index', __name__)

@bp.route('/')
def home():
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

    return render_template('home.html')

@bp.route('/<int:channel_id>/channels', methods=('GET', 'POST'))
@login_required
def channels(channel_id):
    user_channels = g.user.channels()
    messages = Channel.get_messages(channel_id)
    users = {user[0]:user[1] for user in DB.exec("SELECT id,username from users")}
    output_messages = []
    for message in messages:
        output_messages.append( (users[message[1]], message[2]) )
    return render_template('channels.html', chs=user_channels, channel_id=channel_id, messages=output_messages)


@bp.route('/new_channel', methods=('GET', 'POST'))
@login_required
def new_channel():
    if request.method == 'POST':
        channel_name = request.form['name']
        error = None
        if not channel_name:
            error = 'Name is required'
        if error is not None:
            flash(error)
        else:
            Channel.create(channel_name)
            new_ch = Channel.find(channel_name)
            new_ch.add_user(g.user.id)
            user_channels = g.user.channels()
            return render_template('channels.html', chs=user_channels, channel_id=new_ch.id)
    return render_template('new_channel.html')
    #return render_template('channels.html', chs=user_channels)

@bp.route('/test-message', methods=('GET', 'POST'))
def receive_message():
    messages = Message.all()
    return render_template('test-message.html', messages = messages)


@bp.route('/post_message', methods=('GET', 'POST'))
@login_required
def post_new_message():
    print("hi")
    if request.method == 'POST':
        message = request.form['message']
        channel_id = request.form['channel_id']
        Message.create(g.user.id, channel_id, message)
    return redirect( url_for("index.channels", channel_id=channel_id) )