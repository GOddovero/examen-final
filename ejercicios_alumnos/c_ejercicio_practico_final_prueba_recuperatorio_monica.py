"""
Recuperatorio examen final!
Nombre y Apellido: Mónica Marina Buffoni
Edad: 44
DNI: 27632290
Email:
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario.
#Resultado esperado: Hola, {NombreUsuario}! Bienvenido!. Siendo NombreUsuario el nombre ingresado por teclado.  
#Cantidad errores: 3
nombre_usuario = input("Ingrese su nombre: ")
print(f"Hola, {nombre_usuario}! Bienvenido!")
# en le print falta f
# nombre va en minusculas por que es una variable

#Ejercicio 2: Promedio de 4 numeros. 
#Resultado esperado: El promedio de 4 numeros, si ingreso 5-10-7-8 el promedio deberia imprimir 7,5
#Cantidad errores: 5
num1 = int("input(Ingrese el primer número: ")
num2 = int("input(Ingrese el segundo número: ")
num3 = int("input(Ingrese el tercer número: ")
num4 = int("input(Ingrese el cuarto número: ")
promedio= (num1 + num2 + num3 + num4)/ 3 #Falta: falto cambiar la cantidad de numeros en el promedio => de 3 a 4
print(f"El promedio es: ,{promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Salida: Si la calificacion ingresada es mayor o igual que 6: El estudiante ha aprobado, Si no, El estudiante ha reprobado.
#Cantidad de errores: 3

calificacion = input("Ingrese la calificación del estudiante: ")
if calificacion >= 6:
    texto = "El estudiante ha aprobado"
else:
    texto= "El estudiante ha reprobado"
print(texto)

#Ejercicio 4: Lista de Compras.
#Salida esperada: La cantidad en numeros de items en la lista de compras! RECORDA: usar el len
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)

print("Lista de compras:")
for item in lista_compras: #Falta el len()
    print("- " + lista_compras[i]) #Falta: no devuelve nada, si usas [i] como indice, en el for tenes que utilizar lo mismo no item.

#Ejercicio 5: Clase Circulo.
#Salida esperada: 78.53975
#Cantidad de errores: 5

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * radio ** 2 #Falta: el radio es self.radio

Mi_circulo = Circulo(5) #Falta: el nombre de la variable no esta en snake case
print(f"El área del círculo es: {mi_circulo.calcular_area()}")


#Ejercicio 6: Generar un numero Aleatorio.
#Salida esperada: El número aleatorio generado es: (un numero generado aleatoreamente)
#Cantidad de errores: 3
import random
numero = random.randint(1, 10)
print("El número aleatorio generado es: ", + numero)

#Ejercicio 7: Contar Vocales en una Cadena:
#Número de vocales en la cadena:  4
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower()in vocales:
        contador =+1 #Falta: el operador de asignacion es += no =+

print("Número de vocales en la cadena: ", contador)

#Ejercicio 8: Funcion para repetir cadenas.
#Salida esperada: Al ingresar como texto Hola y 3 como cantidad de veces a repetir, deberia imprimir: El texto repetido es: HolaHolaHola
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado

texto = input("Ingrese un texto: ")
repeticiones = int("input¿Cuántas veces desea repetir el texto? ") #Falta: el input tiene que ir fuera de las comillas y con ()
print(f"El texto repetido es: {repetir_cadena},(texto, repeticiones)") #Falta, pasarle por argumento a repetir_cadena el texto y repeticiones

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.
"""
Salida esperada:
Nombre: Gaspar, Edad: 23, Profesion: Profesor
Nombre: Diego, Edad: 45, Profesion: Desarrollador de Software
Nombre: Fermin, Edad: 16, Profesion: Estudiante
Es mayor de edad
Es mayor de edad
No es mayor de edad (Este varia dependiendo de la tercer persona ingresada)
"""
class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

        def imprimir(self): #Falta, esta mal identado
            print(f"Nombre: {self.nombre}, Edad: {self.edad}, Profesión: {self.profesion}")
            
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return "Es mayor de edad"
        else:
            return "No es mayor de edad"
    
persona_1= Persona(" Gaspar", 23, "Profesor")
persona_2= Persona("Diego", 45, "Desarrollador de Sofware")
persona_3= Persona("Mónica", 44, "Estudiante")

persona_1.imprimir()
persona_2.imprimir()
persona_3.imprimir()

print("persona_1.es_mayor_de_edad()") #Falta: no lleva comillas ya que invocamos a un metodo, no un texto
print("persona_2.es_mayor_de_edad()")
print("persona_3.es_mayor_de_edad()")
