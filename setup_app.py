from flask import Flask

app = Flask(__name__)


def setup_app():
    app.config['MYSQL_HOST'] = '0.0.0.0'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'teluni12'
    app.config['MYSQL_DB'] = 'jogoteca'
    app.config['MYSQL_PORT'] = 3306

    return app
