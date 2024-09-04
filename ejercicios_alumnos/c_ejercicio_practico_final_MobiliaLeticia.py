"""
Nombre y Apellido: Leticia Ivana Mobilia
Edad:
DNI:29.972.256
Email: letimobilia@hotmail.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
nombre_usuario = input("Ingrese su nombre: ")
print(f"Hola, {nombre_usuario}! Bienvenido!")

#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
#Falta un numero completo, el ejercicio ingresar 4 números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = int(input("Ingrese la calificación del estudiante: "))
texto = "El estudiante ha aprobado"
if calificacion >= 6:
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

print("Lista de compras:")
cantidad = len(lista_compras)
for i in range(cantidad):
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5
class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = 3.14159 * self.radio ** 2 #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.
        return area
        
mi_circulo = Circulo(5)
print(f"El área del círculo es: {mi_circulo.calcular_area()}")


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
import random
numero = random.randint(1,10)
print(f"El número aleatorio generado es: {numero}")


#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = ["a","e","i","o","u"] #Esta bien, pero no hace faltä convertirlo a lista.
contador = 0

for letra in cadena:
    if letra.lower() in vocales:
        contador += 1

print(f"Número de vocales en la cadena: {contador}")

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado

texto = input("Ingrese un texto: ")
repeticiones = int(input("¿Cuántas veces desea repetir el texto? "))
print(f"El texto repetido es: {repetir_cadena(texto, repeticiones)}")

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad."""
class Persona:

def__init__(self, nombre, edad, profesion) #Falta: Esta mal identado y faltan los dos puntitos al final.
self.nombre = nombre
self.edad = edad
self.profesion = profesion

def imprimir(self):
    print(f"Nombre es {nombre}, edas es {edad}, profesion es {profesion}")

gaspar = Persona(Gaspar, 23, Profesor) #Falta: Tanto Gaspar como profesor son cadenas de texto, hay que pasarlo como "Gaspar" y "Profesor"
diego = Persona(Diego, 45, Desarrollador de software) #Falta: Tanto Gaspar como profesor son cadenas de texto, hay que pasarlo como "Diego" y "Desarrollador de software"
#Falta una instancia
#Falta el metodo para saber si es mayor o menor de edad.