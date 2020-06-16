from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap()

from .views import page

def create_app(config):
    app.config.from_object(config)
    bootstrap.init_app(app)
    app.register_blueprint(page) #se busca desde el archivo views.py
    return app
