"""
Nombre y Apellido: Eugenia Beltramone
Edad: 44 años
DNI: 27.632.272
Email: mebeltramone1979@gmail.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3

nombre_usuario = input("Ingrese su nombre:" )
print(f"Hola, {nombre_usuario}! Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5

import funciones as f 

num_1 =f.validar_numero ()
num_2 = f.validar_numero ()
num_3 =  f.validar_numero ()
num_4 = f.validar_numero ()


suma = (num_1 + num_2 + num_3 + num_4) 
promedio = (suma /4)
print(f"El promedio es: {promedio}")


#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3



calificacion = f.ingresar_numero("Ingrese la calificación del estudiante: ")

if calificacion >= 6:
    texto = "El estudiante ha aprobado"
    print(texto)
else:
    texto= "El estudiante ha reprobado"
    print(texto)

#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)
    lista = len(lista_compras)
    

print("Lista de compras:")
for i in range(lista):
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
    
        
        return 3.14159 * self.radio ** 2 #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.

mi_circulo = Circulo(5)
print(f"El área del círculo es: { mi_circulo.calcular_area()}")


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
import random

numero = random.random ()
print(f"El número aleatorio generado es: +{numero}" )

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in  cadena:
    if letra.lower() in vocales:
        contador += 1

print(f"Número de vocales en la cadena: {contador} ")

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return  resultado

texto = input("Ingrese un texto: ")
repeticiones = int(input("¿Cuántas veces desea repetir el texto? "))
print  (f"El texto repetido es:{repetir_cadena(texto,repeticiones)}" )

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.

class Persona:
    def __init__(self, nombre, edad, profesion):
        
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
    def imprimir(self):
        print (f"nombre: {self.nombre}, edad {self.edad}, profesion: {self.profesion}")
        return

        
    def mayor (self):
        if self.edad >= 18: 
            print (f"{self.nombre} Es mayor de edad")
    
        elif self.edad < 18: 
            print (f"{self.nombre} Es menor de edad")
            
        return
            
            
persona_1 = Persona ("Gaspar", 23, "Profesor")
persona_2 = Persona ("Diego", 45, "Desarrollador de Software")
persona_3 = Persona ("Eugenia", 44, "Profesora")

persona_1.imprimir()
persona_2.imprimir()
persona_3.imprimir()

persona_1.mayor()
persona_2.mayor()
persona_3.mayor()