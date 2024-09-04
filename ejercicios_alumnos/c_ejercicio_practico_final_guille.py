"""
Nombre y Apellido: Guillermo Cochrane   
Edad: 42
DNI: 28813563
Email: guilleac81@gmail.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
# errrores encontrados: 
# comilla linea 13, NombreUsuairo = al estar en mayusculas es una constante, no una variable
# linea 14 falta f en el print,
# NombreUsuario debe definirse en snake_case
print("1)- \n")
nombre_usuario = input("Ingrese su nombre: ")
print(f"\nHola, {nombre_usuario}! Bienvenido!") 

print("\n -------------- \n")
#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
# 3 errores, num1 , num2 y num3 devuelven un valor de tipo string, no un numero
# falta una variable
# PROMEDIO = debe ir en minusculas
# modificar formula de promedio, para agregar la variable y dividir  x 4
# la formula debe ser promedio = (num1 + num2 + num3 + num4) / 4
print("2)- \n")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

promedio = (num1 + num2 + num3 + num4) / 4
print(f"\nEl promedio es: {promedio}")

print("\n -------------- \n")
#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

# calificacion debe ser un numero, no un string
# calificacion debe ser >= 6
# se repite el mensaje de aprobado (?)
print("3)- \n")
calificacion = int(input("Ingrese la calificación del estudiante: "))
texto = "\nEl estudiante ha aprobado"
if calificacion >= 6:
    pass  #print(texto) 
else:
    texto= "\nEl estudiante ha reprobado"

print(texto)

print("\n -------------- \n")
#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1

#error range tiene que ser un numero entero, no una lista

#ver despues
print("4)- \n")
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)

print("Lista de compras:")
for i in range(len(lista_compras)):
    print("- " + lista_compras[i])

print("\n -------------- \n")
#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5
#init mal definido
# no se ingreso en el __init__ el radio
# en calcular area, a radio le falta el self
# Mi_circulo debe ir en minusculas para ser una variable
# en el print falta el +
# mi_circulo.calcular_area() debo converitilo a string
print("5)- \n")
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2 #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.

mi_circulo = Circulo(5)
print("\nEl área del círculo es: " + str(mi_circulo.calcular_area()))

print("\n -------------- \n")
#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
#falta importar random
#numero debe ser str
#el metodo de random  es randint, no randit
print("6)- \n")
import random
numero = random.randint(1, 10)
print("\nEl número aleatorio generado es: " + str(numero))

print("\n -------------- \n")
#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4
# falta el : en el for
# falta el + en el contador, para que sea +=
# falta el + en el print
# hay que converitr a string el contador
# letra.lower() en lugar de  letra.lower 
print("7)- \n")
cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower() in vocales:
        contador += 1
print(f"la cadena es: {cadena} ")
print("\nNúmero de vocales en la cadena: " + str(contador))

print("\n -------------- \n")
#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
# repeticiones debe set int 
# la funcion debe retornar resultado
# a repetir_cadena le falto ingresar las variables
print("8)- \n")
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado

texto = input("Ingrese un texto: ")
repeticiones = int(input("¿Cuántas veces desea repetir el texto? "))
print(f"\nEl texto repetido es: {repetir_cadena(texto, repeticiones)}")

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.
print("9)- \n")
class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def imprimir_nombre(self):
        print(self.nombre)
        return

    def imprimir_edad(self):
        print(self.edad)
        return

    def imprimir_profesion(self):
        print(self.profesion)
        return

    def mayor_edad(self):
        if self.edad > 18:
            return True
        else:
            return False
    
    def mensaje_mayor_edad(self):
        if self.mayor_edad():
            return f"El usuario {self.nombre} es mayor de edad"
        else:
            return f"El usuario {self.nombre} no es mayor de edad"


gaspar = Persona("Gaspar", 23, "Profesor")
diego = Persona("Diego", 45, "Desarrollador de Software")
tu = Persona("Guille", 18, "Estudiante")

gaspar.imprimir_nombre()
gaspar.imprimir_edad()
gaspar.imprimir_profesion()

diego.imprimir_nombre()
diego.imprimir_edad()
diego.imprimir_profesion()

tu.imprimir_nombre()
tu.imprimir_edad()
tu.imprimir_profesion()

print(gaspar.mensaje_mayor_edad())
print(diego.mensaje_mayor_edad())
print(tu.mensaje_mayor_edad())