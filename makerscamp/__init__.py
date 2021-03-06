import os
from flask import Flask
from flask_socketio import SocketIO


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='super_secret_key',
        DATABASE=os.path.join(app.instance_path, 'acebook.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    global socketio
    socketio = SocketIO(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    

    @app.route('/test')
    def test():
        return 'Hi, Test!'

    from .classes import db
    db.init_app(app)

    from .controllers import auth
    app.register_blueprint(auth.bp)

    from .controllers import index
    app.register_blueprint(index.bp)
    app.add_url_rule('/', endpoint='home')

    socketio.run(app)
    return app