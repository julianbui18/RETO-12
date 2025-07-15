import requests

# Función para imprimir pares clave:valor
def imprimir_pares(diccionario):
    for clave in diccionario:
        print(clave, ":", diccionario[clave])

# API 1: randomuser.me
print("API 1: Usuario aleatorio")
respuesta1 = requests.get("https://randomuser.me/api/")
datos1 = respuesta1.json()
print("JSON completo:")
print(datos1)

usuario1 = datos1["results"][0]
print("Pares clave:valor del usuario:")
imprimir_pares(usuario1)
print(" ")

# API 2: Chiste corto
print("API 2: Chiste corto (setup + punchline)")
respuesta2 = requests.get("https://official-joke-api.appspot.com/random_joke")
datos2 = respuesta2.json()
print("JSON completo:")
print(datos2)

print("Pares clave:valor del chiste:")
imprimir_pares(datos2)
print(" ")

# --------- API 3: Nationalize.io ---------
print("API 3: Nacionalidad probable del nombre 'nathaniel'")
respuesta3 = requests.get("https://api.nationalize.io/?name=nathaniel")
datos3 = respuesta3.json()
print("JSON completo:")
print(datos3)

print("Pares clave:valor del nombre:")
imprimir_pares(datos3)
print(" ")

