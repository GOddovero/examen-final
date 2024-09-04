"""
Nombre y Apellido: Florencia Valentina Miranda
Edad:
DNI:31767186
Email:flopi1986@hotmail.com.ar
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
NombreUsuario = input("Ingrese su nombre:" ) #Falta: el nombre de la variable no esta en snake_case.
print(f"Hola, {NombreUsuario}! Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
#Falta: un numero entero, el ejercicio pedia el promedio de 4 números.
num1 = int (input("Ingrese el primer número: "))
num2 = int (input("Ingrese el segundo número: "))
num3 =int (input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = int (input("Ingrese la calificación del estudiante: "))
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
for i in range (len(lista_compras)):
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def __init__(self,radio):
        self.radio = radio

    def calcular_area(self):
        area = 3.14159 * (self.radio**2) #Muy bien los parentesis, pero no hacen falta ya que el orden de prioridad de las operaciones, primero se hace el exponente y despues la multiplicacion.
        return area
Mi_circulo = Circulo(5)
print(f"El área del círculo es:{Mi_circulo.calcular_area()}")


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
import random
numero = random.randint(1, 10)
print("El número aleatorio generado es: " {numero}) #Falta: El print explota, falta agregar la f adelante y mover las comillas.

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower() in vocales:
        contador += 1

print("Número de vocales en la cadena:  {contador}") #Falta: esta mal el print, falta agregar la f adelante. print(f"Número de vocales en la cadena: {contador}")

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado

texto = input("Ingrese un texto: ")
repeticiones = int (input("¿Cuántas veces desea repetir el texto? "))
print(f"El texto repetido es: {repetir_cadena(texto,repeticiones)}")

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.

class Persona(): #Falta: Las clases no se declaran con (), es simplemente class Persona:
    def __init__(self,nombre,profesion,edad):
        self.nombre = nombre
        self.profesion = profesion
        self.edad = edad
    def imprimir_nombre(self):
        print(f"el nombre es{self.nombre}")
        return
    def imprimir_edad(self):
        print(f"la edad es{self.edad}")
        return
    def imprimir_profesion(self):
        print(f"la profesion es{self.profesion}")
        return
    #Falta un metodo para saber si la persona es mayor de edad.
    #Falta crear las tres instancias de la clase persona. (Gaspar, Diego y Tu Nombre)

