# RETO 12 - DICCIONARIOS
1. Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

  **PASOS**
  * Crear o recibir el diccionario.
  * Extraer todos los valores del diccionario.
  * Ordenar esos valores en forma ascendente.
  * Imprimirlos uno por uno.

**SOLUCION**
```python
# Diccionario con algunos valores
datos = {"uno": 5, "dos": 2, "tres": 9, "cuatro": 1}
# Sacar los valores del diccionario
valores = list(datos.values())
# Ordenar los valores
for vuelta in range(len(valores)):
    for posicion in range(len(valores) - 1):
        if valores[posicion] > valores[posicion + 1]:
            # Intercambiar los valores si están en desorden
            auxiliar = valores[posicion]
            valores[posicion] = valores[posicion + 1]
            valores[posicion + 1] = auxiliar
# Imprimir los valores ya ordenados
print("Los valores ordenados son:")
for valor in valores:
    print(valor)
```
2. Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.

**SOLUCION**
```python
# Función para mezclar dos diccionarios
def mezclar_diccionarios(dic1, dic2):
    nuevo_diccionario = {}
    # Primero metemos todo lo del segundo diccionario
    for clave in dic2:
        nuevo_diccionario[clave] = dic2[clave]
    # Luego metemos todo lo del primero, así si hay claves iguales se reemplazan por el valor del primero
    for clave in dic1:
        nuevo_diccionario[clave] = dic1[clave]

    return nuevo_diccionario

# Diccionarios
diccionario1 = {"a": 1, "b": 2, "c": 3}
diccionario2 = {"b": 9, "d": 4}

resultado = mezclar_diccionarios(diccionario1, diccionario2)

# Imprimir el resultado
print("Diccionario mezclado:")
print(resultado)
```
3. Dado el JSON:
```python
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "Diaz Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["Futbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
Cree un programa que lea de un archivo con dicho JSON y:
* Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
* Imprima los nombres completos (nombre y apellidos) de las personas que estén en un rango de edades dado por el usuario.

**SOLUCION**

Aqui primero se guardo el codigo anterior con extension ```.json``` para poder importarlo al codigo y asi usarlo
```python
import json

# Abrir y leer el archivo JSON
with open("infopersonas.json", "r") as archivo:
    datos = json.load(archivo)

# Buscar por deporte 
# Ingresar un deporte
deporte_buscado = input("Ingrese un deporte para buscar: ")

print("Personas que practican", deporte_buscado + ":")

for usuario in datos:
    persona = datos[usuario]
    if deporte_buscado in persona["deportes"]:
        nombre_completo = persona["nombres"] + " " + persona["apellidos"]
        print("-", nombre_completo)

# Buscar por rango de edad 

# Ingresar rango de edades
edad_minima = int(input("Edad mínima: "))
edad_maxima = int(input("Edad máxima: "))

print("Personas entre", edad_minima, "y", edad_maxima, "años:")

for usuario in datos:
    persona = datos[usuario]
    edad = persona["edad"]
    if edad > (edad_minima - 1) and edad < (edad_maxima + 1):
        nombre_completo = persona["nombres"] + " " + persona["apellidos"]
        print("-", nombre_completo)
```
4. A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.

**SOLUCION**

Para esto, primero fue necesario instalar una libreria externa, que es ```requests```, sirve para poder conectarte a internet y en este caso poder accerder a los links de los API's.

Se instalo poniendo en la consola lo siguiente:
```python
pip install requests
```

Ya teniendo esto instalado podra funcionar codigo.

```python
# Importamos la librería "requests" para poder conectarnos a internet y usar APIs
import requests
# Esta función sirve para mostrar todos los pares clave:valor de un diccionario
def imprimir_pares(diccionario):
    for clave in diccionario:
        print(clave, ":", diccionario[clave])

# API 1: randomuser.me
# Nos conectamos a la API que da un usuario aleatorio
print("API 1: Usuario aleatorio")
respuesta1 = requests.get("https://randomuser.me/api/")  # Hacemos la solicitud
datos1 = respuesta1.json()  # Convertimos la respuesta a formato JSON
print("JSON completo:")  # Mostramos el JSON completo
print(datos1)

# Como los datos vienen dentro de una lista llamada 'results', tomamos el primer usuario
usuario1 = datos1["results"][0]

# Imprimimos los pares clave:valor de ese usuario
print("Pares clave:valor del usuario:")
imprimir_pares(usuario1)

print(" ")

# API 2: official-joke-api
# Nos conectamos a la API que da un chiste con setup y punchline
print("API 2: Chiste corto (setup + punchline)")
respuesta2 = requests.get("https://official-joke-api.appspot.com/random_joke")  # Solicitud
datos2 = respuesta2.json()  # Convertimos la respuesta a JSON
print("JSON completo:")  # Mostramos todo el JSON
print(datos2)

# Imprimimos los pares clave:valor del chiste
print("Pares clave:valor del chiste:")
imprimir_pares(datos2)

print(" ")

# API 3: nationalize.io
# Esta API nos dice de qué país puede ser un nombre (en este caso: "nathaniel")
print("API 3: Nacionalidad probable del nombre 'nathaniel'")
respuesta3 = requests.get("https://api.nationalize.io/?name=nathaniel")  # Solicitud
datos3 = respuesta3.json()  # Convertimos a JSON
print("JSON completo:")
print(datos3)

# Imprimimos los pares clave:valor del JSON
print("Pares clave:valor del nombre:")
imprimir_pares(datos3)

print(" ")
```
5. (Opcional) El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:
```python
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)
```
Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' (aquí pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viuento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.

**SOLUCION**
```python
import json
from datetime import datetime

# Aquí va el JSON con los datos del clima
texto_clima = '''
{
  "dt": {"0": 1685116800, "1": 1685203200, "2": 1685289600, "3": 1685376000, "4": 1685462400, "5": 1685548800, "6": 1685635200, "7": 1685721600},
  "alertPrecip": {"0": "X", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
  "alertAlertas": {"0": "-", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
  "alertVelViento": {"0": "-", "1": "-", "2": "X", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
  "alertTmpMax": {"0": "-", "1": "-", "2": "-", "3": "-", "4": "-", "5": "X", "6": "-", "7": "-"},
  "alertTmpMin": {"0": "-", "1": "X", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
  "prcp": {"0": 40.0, "1": 1.65, "2": 14.01, "3": 5.07, "4": 16.55, "5": 2.17, "6": 2.77, "7": 1.73},
  "velViento": {"0": 3.56, "1": 5.07, "2": 5.38, "3": 3.95, "4": 4.74, "5": 3.75, "6": 4.08, "7": 5.94},
  "tmpMax": {"0": 27.16, "1": 31.1, "2": 30.2, "3": 29.5, "4": 28.87, "5": 29.78, "6": 28.96, "7": 28.25},
  "tmpMin": {"0": 25.64, "1": 24.64, "2": 25.84, "3": 25.56, "4": 25.72, "5": 24.86, "6": 25.96, "7": 25.47}
}
'''

# Convertimos el texto JSON a un diccionario
clima = json.loads(texto_clima)

# Diccionario con tipos de alerta y sus datos
tipos_alerta = {
    "alertPrecip": {"nombre": "Lluvias", "dato": "prcp", "unidad": "mm"},
    "alertVelViento": {"nombre": "Viento fuerte", "dato": "velViento", "unidad": "m/s"},
    "alertTmpMax": {"nombre": "Temperatura máxima", "dato": "tmpMax", "unidad": "°C"},
    "alertTmpMin": {"nombre": "Temperatura mínima", "dato": "tmpMin", "unidad": "°C"},
    "alertAlertas": {"nombre": "Alerta general", "dato": "ninguno", "unidad": ""}
}

# Función para convertir fecha en formato legible
def convertir_fecha(numero_unix):
    return datetime.utcfromtimestamp(numero_unix).strftime('%Y-%m-%d')

# Recorremos los 8 días
for dia_actual in range(8):
    for nombre_alerta in tipos_alerta:
        # Revisamos si hay una alerta marcada con "X"
        if clima[nombre_alerta][str(dia_actual)] == "X":
            fecha = convertir_fecha(clima["dt"][str(dia_actual)])
            nombre_evento = tipos_alerta[nombre_alerta]["nombre"]
            dato_relacionado = tipos_alerta[nombre_alerta]["dato"]

            # Verificamos si tiene valor asociado o no
            if dato_relacionado != "ninguno":
                valor = clima[dato_relacionado][str(dia_actual)]
                unidad = tipos_alerta[nombre_alerta]["unidad"]
                print("Fecha:", fecha)
                print("Tipo de alerta:", nombre_evento)
                print("Valor:", valor, unidad)
                print(" ")
            else:
                print("Fecha:", fecha)
                print("Tipo de alerta:", nombre_evento)
                print("No tiene valor asociado")
                print(" ")
```

**JULIAN ESTEBAN BUITRAGO CRUZ**
