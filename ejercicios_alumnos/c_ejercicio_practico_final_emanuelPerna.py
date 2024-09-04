"""
Nombre y Apellido: Emanuel Perna
Edad: 32
DNI: 35832494
Email: emanuelperna@icloud.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
nombre_usuario = input("Ingrese su nombre: ")
print(f"Hola, {nombre_usuario}! Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

promedio = (num1 + num2 + num3 + num4) / 4
print(f"El promedio es: {promedio}")


#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = int(input("Ingrese la calificacion del estudiante: "))

if calificacion >= 6:
    print("El estudiante ha aprobado")

else:
    print("El estudiante ha repobado")


#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)

print(f"La lista de compra esta compuesta por: {lista_compras}")
"""
Falta: Falta toda la logica para mostrar el contenido de lista_compras

print("Lista de compras:")
for i in range(len(lista_compras)): #1-Falta agregar el len() para saber cuantos elementos tiene la lista
    print("- " + lista_compras[i])

"""
#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def __init__(self,radio):
        self.radio = radio

    def calcular_area(self):
        pi = (self.radio ** 2) #Falta: esta mal la formula, es pi (3.14159) por el radio al cuadrado
        print(f"El área del círculo es: {pi}")
        return
    
mi_circulo = Circulo(5)
mi_circulo.calcular_area()


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3

import random 

numero = random.randint(1, 10)
print(f"El número aleatorio generado es: {numero}")


#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower() in vocales:
        contador += 1

print(f"Número de vocales en la cadena: {contador}" )

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3


def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado

texto = input("Ingrese un texto: ")
repeticiones = int(input("¿Cuántas veces desea repetir el texto? "))
print(f"El texto repetido es: {repetir_cadena (texto,repeticiones)}")


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
        pass

    def mostrar_nombre(self):
        print(f"El nombre de la persona ingresada es: {self.nombre}")
        return
    
    def mostrar_edad(self):
        print(f"La edad de la persona ingresada es: {self.edad}")
        return
    
    def mostrar_profesion(self):
        print(f"La profesion de la persona ingresada es: {self.profesion}")
        return
    
    def mostrar_edades(self):
        if self.edad >= 18:
            print("La persona ingresada es mayor de edad")
        else:
            print("La persona ingresada es menor de edad")
        return

personas = Persona("Gaspar", 23, "Profesor")
personas.mostrar_nombre()
personas.mostrar_edad()
personas.mostrar_profesion()
personas.mostrar_edades()


personas = Persona("Diego", 45, "Desarrollador de Software")
personas.mostrar_nombre()
personas.mostrar_edad()
personas.mostrar_profesion()
personas.mostrar_edades()


personas = Persona("Emanuel", 32, "Estudiante")
personas.mostrar_nombre()
personas.mostrar_edad()
personas.mostrar_profesion()
personas.mostrar_edades()

