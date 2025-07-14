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
