"""
Nombre y Apellido: Franco Aguado
Edad: 40
DNI: 30596753
Email: franco@teconet.com.ar
"""
import funciones_capo as fc

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:
#Ejercicio 1: Saludar usuario.
#Cantidad errores: 3
nombre_usuario = input("Ingrese su nombre: ")
print(f"Hola, {nombre_usuario}! Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros.
#Cantidad errores: 5
numero_1 = fc.ingresar_numero("Ingrese el primer número: ")
numero_2 = fc.ingresar_numero("Ingrese el segundo número: ")
numero_3 = fc.ingresar_numero("Ingrese el tercer número: ")

promedio = (numero_1 + numero_2 + numero_3)/3
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = fc.ingresar_numero("Ingrese la calificación del estudiante: ")
aprobado = "El estudiante ha aprobado"
desaprobado = "El estudiante ha desaprobado"

if calificacion >= 6:
    print(aprobado)
else:
    print(desaprobado)

#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1

lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)

print("Lista de compras:")
for lista in lista_compras:
    print("- " + lista)

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def __init__(self):
        radio = fc.ingresar_numero("Ingrese el radio en CM. del circulo a calcular : ")
        self.radio = radio
        pass
    def calcular_area(self):
        area = 3.14159 * self.radio ** 2 #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.
        return print(f"El área del círculo es: {area} CM")

mi_circulo = Circulo()
mi_circulo.calcular_area()

#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3

import random # Esto deberia ir arriba , junto al otro random
numero = random.randint (1,10)
print(f"El número aleatorio generado es: {numero}")

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra in vocales:
        contador += 1
    else:
        continue
print (f"Número de vocales en la cadena: {contador}")

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3

def repetir_cadena (cadena:str, veces:int)->str:
    resultado = cadena * veces
    return resultado

texto = input("Ingrese un texto: ")
repeticiones = fc.ingresar_numero("¿Cuántas veces desea repetir el texto? ")
print(f"El texto repetido es: {repetir_cadena(texto, repeticiones)}")

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.

class Persona:
    def __init__(self):
        nombre = input("Ingrese su nombre : ")
        edad = fc.ingresar_numero("Ingrese su edad : ")
        profecion = input("Ingrese su profecion : ")
        self.nombre = nombre
        self.edad = edad
        self.profecion = profecion
        pass
    def imprimir_nombre (self):
        print(f"Su nombre es : {self.nombre}")
        return
    def imprimir_edad (self):
        print(f"Su edad es : {self.edad}")
        return
    def imprimir_profecion (self):
        print(f"Su profecion es : {self.profecion}")
        return
    def mayor_menor (self):
        if self.edad >= 18:
            print("Usted es mayor de edad ")
        else:
            print("Usted es menor de edad")

persona = Persona()
persona.imprimir_nombre()
persona.imprimir_edad()
persona.imprimir_profecion()
persona.mayor_menor()