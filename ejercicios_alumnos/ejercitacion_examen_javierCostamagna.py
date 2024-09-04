"""
Nombre y Apellido: Javier Costamagna
Edad: 49
DNI: 24.585.600
Email: jrcosta75@gmail.com
"""
import random #Importamos la libreria RANDOM
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
    else:
        lista_compras.append(item)

print(f"Lista de compras: {lista_compras}")
for lista in lista_compras:
    print(lista)

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def __init__(self,radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2 #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.

mi_circulo = Circulo(5)
area = mi_circulo.calcular_area()
print(f"El área del círculo es: {area}")


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
numero = random.randint(1,10)
print(f"El número aleatorio generado es:  {numero}")

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
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
    def __init__(self,nombre, edad, profesion) -> None:
        self.nombre = nombre
        self.edad = edad 
        self.profesion = profesion
        
    
    def imprimir(self): 
        print (f"El nombre es {self.nombre}, tiene {self.edad} de edad y trabaja de {self.profesion}")
        return
    
    def mayor_edad(self):
        if self.edad >= 18:  
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} es menor de edad")
        return
    
    

persona1 = Persona("Gaspar", 23, "Profesor")
persona2 = Persona("Diego", 45, "Desarrollador de Software")

Persona.imprimir(persona1)
Persona.mayor_edad(persona1)
Persona.imprimir(persona2)
Persona.mayor_edad(persona2)
