# importamos el modulo de json
import json
# abrimos el archivo "config.json" en formato r que significa en formato de lectura
configjson = open("config.json", "r")
contraseña_json = configjson.read() #<---( convertimos la variable "configjson" en formato de lectura con el metodo "read()"
contraseña_server = json.loads(contraseña_json) #<---(llamamos el metodo de json y con la funcion "loads", leemos la key que se encuentra en la variable "contraseña_json"
configjson.close() #<---(cerramos el archivo del "config.json"