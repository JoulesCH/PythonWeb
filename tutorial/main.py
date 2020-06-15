from flask import  Flask
from flask import render_template, request

app = Flask(__name__)

@app.before_request #decorador
def before_request(): #puede conectarse a base de datos, consultas, etc.
    print("Antes de la petición")

@app.after_request
def after_request(response): #parametro response es el return de las funciones
    print("Despues de la petición")
    return response

@app.route('/')
def index():
    name = 'Codi'
    is_premium = False
    course = 'Python Web'
    courses = ['Python','Ruby','Java','Elixir']
    return render_template('index.html',username = name,is_premium = is_premium,course_name = course,courses = courses)

@app.route('/usuario/<username>/<int:num>') #parametros
def usuario(username,num):
    return 'Hola ' + username + ' Numero: ' + str(num)

@app.route('/about')
def about():
    return render_template('about.html')


#Request le llegan datos mediante el url /datos?variable1=''&variable2=''
@app.route ('/datos')
def datos():
    nombre = request.args.get('nombre','') #Diccionario, '' indica que poner si no hay variable nombre
    curso = request.args.get('curso','') #
    return 'Listado de datos ' + nombre + 'curso: ' + curso


if __name__ == '__main__':
    app.run(debug=True) #debug indicamos que el servidor nos arroje errores
    #appp.run(debug=True,port=9000) #indicamos en que puerto lo queremos
