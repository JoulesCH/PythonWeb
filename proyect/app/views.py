#modelo vista - controlador
#blueprint - aplicaciones modulares
from flask import Blueprint
from flask import render_template
from .forms import LoginForm

page = Blueprint('page',__name__)

@page.app_errorhandler(404) #decoramos la funcion con errorhandler para manegar el 404
def page_not_found(error):
    return render_template('errors/404.html'), 404 #status 200: exito

@page.route('/')
def index():
    return render_template('index.html',title='Para Julieta')

@page.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html',title='Login',form=form)
