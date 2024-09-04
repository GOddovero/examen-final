"""
Nombre y Apellido: Shirley Rodriguez
Edad: 31        
DNI: 37126510
Email: reverenge_09@hotmail.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
nombre_usuario = input ("Ingrese su nombre: ")
print (f"Hola {nombre_usuario}! Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = int(input("Ingrese la calificación del estudiante: "))
texto = "El estudiante ha aprobado"
if calificacion >= 6:
    print(texto)
else:
    print("El estudiante ha reprobado")

#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    else:
        lista_compras.append(item)

print("La Lista de compras es:c")

for lista in lista_compras:
    print("- " + {lista_compras})

sin hacer - va el len ()



#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def __init__(self,radio,): 
        self.radio = radio


    def calcular_area(self):
        self.area = 3.14159 * (self.radio ** 2) #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.
        print(f"El área del círculo es: {self.area}")

        return  


Circulo = Circulo(5)
Circulo.calcular_area()


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3

import random
numero = random.randint(1, 10)
print(f"El número aleatorio generado es: {numero} ")


#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letras in cadena:
    if letras.lower() in vocales:
        contador = contador + 1

print(f"Número de vocales en la cadena: {contador}")

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado

cadena = input("Ingrese un texto: ")
veces = int(input("¿Cuántas veces desea repetir el texto? "))

print(f"El texto repetido es: {repetir_cadena(cadena,veces)}")


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
        
    def datos (self):
        print(f"El nombre es {self.nombre}, su edad es {self.edad} años, y se dedica a ser {self.profesion}. ")
        
    
    if edad >= 18:
        print ("La persona es mayor de edad.")
    else:
        print ("La persona es menor de edad.")

Uno = Persona("Diego",44,"Programador")
Dos = Persona("Gaspar",23,"Profesor")
Tres = Persona("Shirley",31,"Empleada")
