"""
Nombre y Apellido: Fermin Fauda
Edad: 15
DNI: 48815486
Email: ferminfauda9@gmail.com
"""


#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
Nombre_usuario = input("Ingrese su nombre: ")
print(f"Hola, {Nombre_usuario}! Bienvenido!")

#Falto cambiar el nombre de la variable, va nombre_usuario, en snake case va todo en minusculas



#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
#Falta, un numero completo, porque el ejercicio pide 4 input. 
while True:
    Numero1 = input("Ingrese el primer número: ")
    Numero2 = input("Ingrese el segundo número: ")
    Numero3 = input("Ingrese el tercer número: ")
    if Numero1.isdigit() and Numero2.isdigit() and Numero3.isdigit():
        Numero1 = int(Numero1)
        Numero2 = int(Numero2)
        Numero3 = int(Numero3)
    else:
        print("Uno de los valores no es un numero")
        break

    PROMEDIO = (Numero1 + Numero2 + Numero3) / 3 #Falta cambiar el nombre de variable, ya que en mayusculas es una constante
    print(f"El promedio es: {PROMEDIO}") 
    continuar = input("¿Desea continuar? (escrine NO para salir o cualquier tecla para seguir): ")
    if continuar.upper() == "NO":
        break
#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = input("Ingrese la calificación del estudiante: ")
if calificacion.isdigit:
    calificacion = float(calificacion)

if calificacion < 6: 
    print("El estudiante ha reprobado")
else:
    print("El estudiante ha aprobado")
    

#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    else:
        lista_compras.append(item)

    print("Lista de compras:")
    for i in range (len(lista_compras)):
        print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo():
    def __init__(self,radio):
        self.radio = radio

    def calcular_area(self):
        return (3.14 * (self.radio * self.radio )) #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.

Mi_circulo = Circulo(5)
print(f"El área del círculo es: {Mi_circulo.calcular_area()}") #Falta cambiar el nombre de la variable a snake case


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
        contador +=  1

print(f"Número de vocales en la cadena: {contador}")


#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces, resultado): #Resultado no hace falta pasarlo por parametro
    resultado = cadena * veces
    return resultado
while True:
    texto = input("Ingrese un texto: ")
    repeticiones = (input("¿Cuántas veces desea repetir el texto? "))
    if repeticiones.isdigit():
        repeticiones = int(repeticiones)
    else:
        print("El valor no es un numero")
        break

    repetir = repetir_cadena(texto, repeticiones, "") 
    print(f"El texto repetido es: {repetir}")

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres metodos de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.

class Persona():
    def __init__(self, nombre:str, edad:int, profesion:str):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def imprimir(self):
        print(f"\nEl nombre de la persona es: {self.nombre}")
        print(f"El edad de la persona es: {self.edad}")
        print(f"La profesion de la persona es: {self.profesion}")
    def mayor_edad(self):
        if self.edad > 18:
            print("La persona es mayor de edad")
        else:
            print("La persona no es mayor de edad")

datos_gaspar = Persona("gaspar", 23, "Profesor")
datos_diego = Persona("diego", 45, "Desarrollador de Software")
datos_mios = Persona("Fermin", 15, "Estudiante")

datos_gaspar.imprimir()
datos_gaspar.mayor_edad()
datos_diego.imprimir()
datos_diego.mayor_edad()
datos_mios.imprimir()
datos_mios.mayor_edad()

