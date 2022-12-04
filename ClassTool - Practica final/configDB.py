#importamos el modulo de sqlite3 para administrar la database
import sqlite3
import os # importamos el metodo os para verificar la existencia de archivos dentro del proyecto

if not os.path.exists('basedatos.db'): #<---(condicion que nos creara la base de datos desde cero siempre y cuando esta no exista en la carpeta del proyecto
    
    db = sqlite3.connect('basedatos.db')
    cursor = db.cursor()
    # sentencia de slite3 que nos creara una tabla llamada iniciarsesion con 2 columnas de tipo texto no nulas llamadas "correo" y "contraseña"
    cursor.execute("""
                   CREATE TABLE "iniciarsesion" (
        "correo"	TEXT NOT NULL UNIQUE,
        "contraseña"	TEXT NOT NULL
                   )""")
    print('La base de datos se creo correctamente!') #<---(mensaje para confirmar que la creacion de la database salio todo en orden
else: # si la base de datos existe en el proyecto, entonces no se ejecutara mas nada
    pass