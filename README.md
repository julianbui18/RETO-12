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
```python
