# importamos el modulo de sqlite3 que nos permitira administrar nuestra base de datos
import sqlite3
# importamos las funciones de flash y render_template de flask
from flask import flash, render_template
# creamos una clcase llamada manejoDatos para crear las funciones del login
class manejoDatos():
    # creamos un costructor que contiene como parametros el self para administrar y pasar los datos, y el correo y la contraseña que el usuario pasara mas tarde
    def __init__(self, correo, contraseña):
        # creamos las variables que usaremos en las demas funciones
        self.correo = correo
        self.contraseña = contraseña
        self.baseDatos = sqlite3.connect('basedatos.db', check_same_thread=False)#<---(este "chek_same_thread" lo deshabilitamos para evitar un error en nuestra base de datos debido a multiples procesos
        self.cursor = self.baseDatos.cursor() #<----(con esta funcion del sqlite3 podremos administrar nuestra base de datos ya conectada
    
    #creamos la funcion del login
    def login(self): #<---(le pasamos el parametro activo del constructor "self"
        '''funcion para extraer los datos de las columnas de correo y contraseña y asi hacer una validacion con el cliente de que dichos datos existen y fueron ingresados correctamente, o erroneos en caso de...'''
        #hacemos una peticion de sqlite para seleccionar todos los datos de la columna correo que se encuentra en la tabla de iniciarsesion
        correos_Basedatos = self.cursor.execute('SELECT correo FROM iniciarsesion')
        #extraemos todos los datos de la peticion hecha en la variable de "correos_Basedatos"
        correosExtraidosDB = correos_Basedatos.fetchall()
        
        #creamos un for para recorrer todos los datos de la variable "correosExtraidosDB"
        for extraer_correo in correosExtraidosDB:

            for borrar_caracteresCorreo in extraer_correo: #<---( este for anidado nos permitira eliminar caracteres que salen de la base de datos por default ej de estos caracteres: "[,("
                if borrar_caracteresCorreo == self.correo: # condicion para verificar que el correo ingresado por el usuario existe dentro de todos los usuarios extraidos de la base de datos
                    
                    #si este usuario existe, entonces hacemos una peticion de sqlite de la tabla iniciarsesion, en la columna contraseña, la contraseña del usuario ingresado
                    contraseña_Basedatos = self.cursor.execute(f'SELECT contraseña FROM iniciarsesion WHERE correo="{self.correo}"')
                    contraseñaExtraida = contraseña_Basedatos.fetchall() #<---(extraemos la contraseña de la peticion que se hace en la variable "contraseña_Basedatos"
                    
                    #creamos un for para recorrer los datos extraidos de la variable "contraseñaExtraida"
                    for extraer_contraseña in contraseñaExtraida:
                        for borrar_caracteresContraseña in extraer_contraseña: #<---(creamos un for anidado para eliminar los caracteres que salen por default de la base de datos
                            if borrar_caracteresContraseña == self.contraseña: # <---(condicion para verificar si la contraseña ingresada es la perteneciente al usuario ingresado
                                flash(f'bienvenido {self.correo}', 'success') # <---(con la funcion flash mandaremos al archivo del login.html un mensaje de bienvenida mas el tipo de alerta
                                return render_template('login.html') #<---(retornamos el archivo de login.html
                            # si la contraseña no es correcta, se enviara una alerta de tipo danger que nos dara un mensaje
                            else:
                                flash('la contraseña ingresada no es correcta', 'danger')
                                return render_template('login.html')
                else: #<---(si el usuario ingresado no existe en la base de datos, entonces mandara una alerta de tipo danger
                    flash('el usuario ingresado no es correcto', 'danger')  
                    return render_template('login.html')    
        