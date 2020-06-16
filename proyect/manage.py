from app import create_app #Archivo __init__.py
from flask_script import Manager #Nos permite levantar el servidor apartir de una instancia
from config import config

#Ejecutar archivo: python manage.py runserver
config_class = config['development']
app = create_app(config_class)

if __name__=='__main__':
    manager = Manager(app)
    manager.run()
