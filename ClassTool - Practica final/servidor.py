#Importar el micro-framework de flask y el objeto de request
from flask import Flask, request
#Importamos todos los elementos del archivo "main.py"
from main import *
#Importamos todos los elementos del archivo "configjson.py" que nos ayudara a traer la contraseña del servidor que se guarda en el archivo "config.json"
from configjson import *
#Importamos el archivo "configDB.py", que nos permitira crear la base de datos en caso de que no exista
from configDB import *

#Creamos una variable que tendra el modulo de flask y dentro contendra un nombre
servidor = Flask(__name__)
#Agregamos una llave secreta al servidor
servidor.config['SECRET_KEY']=f'{contraseña_server}'#<---(esta llave secreta proviene del archivo "config.json"
#Creamos la ruta principal
@servidor.route('/')
#Creamos una funcion que retornara el archivo "LandingPage.html" que se encuentra en la carpeta templates
def inicio():
    '''retorna gracias a la funcion que proviene de flask llamada render_template, el archivo html llamado landingPage.html'''
    return render_template('LandingPage.html')

#Creamos la ruta que retornara el archivo de "login.html"
@servidor.route('/login')
#Funcion para retornar el archivo "login.html"
def mostrar_login():
    '''Esta funcion nos ayudara a retornar con render_template el archivo que contiene el login.html que se encuenta en la carpeta templates'''
    return render_template('login.html')

#creamos la ruta para validar los datos del archivo "login.html" y le agregamos los metodos de "GET" y "POST" para traer los datos desde el cliente al servidor
@servidor.route('/validacion', methods=['GET', 'POST'])
def validar_datos():
    '''funcion para traer los datos del form del archivo login.html y asi pasarlo a la clase de manejoDatos'''
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    clase_objeto = manejoDatos(correo, contraseña)
    # retornamos la funcion que se encuentra en la clase importada llamada "manejoDatos"
    return clase_objeto.login()
# condicional creada para asegurarnos de que el servidor se encienda siempre y cuando se ejecute el nombre de este archivo
if __name__ == '__main__':
    #llamamos la variable que contiene el modulo de flask, y le damos 2 parametros a la funcion de run, "debug=true" sirve para realizar y guardar cambios en el servidor sin tener la necesidad de volver a ejecutarlo, "port" es el puerto en el que abrira el servidor 
    servidor.run(debug=True, port=101010)
