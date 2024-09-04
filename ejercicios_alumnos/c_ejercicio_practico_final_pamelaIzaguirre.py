"""
Nombre y Apellido: Pamela Izaguirre
Edad: 36
DNI:33581419
Email: pameiza88@gmail.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
Nombre_Usuario = input( "Ingrese su nombre") #Falta: corregir el nombre de la variable, va en snake_case nombre_usuario
print(f"Hola, {Nombre_Usuario}{Bienvenido!}") #Falta: el bienvenido va sin llaves


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
#Falta transformar los input a int.
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
num3 = input("Ingrese el tercer número: ")
num4 = input("ingrese el cuarto numero:")
promedio =( num1 + num2 + num3 + num4 )/ 4
print(f"El promedio es: {PROMEDIO}") #Falta: cambiar el nombre a la variable

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = input("Ingrese la calificación del estudiante: ") #Falta transformar los input a int.
texto = "El estudiante ha aprobado"
if calificacion <= 6: #Falta: el simbolo esta al reves 
    print(texto)
else:
    texto= "El estudiante ha reprobado"
print(texto) #Falta: solucionar el doble mensaje cuando el estudiante aprueba.

#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)

print("Lista de compras:")
for i in range(lista_compras): #Falta el len en el range
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def __init__(radio): #Falta: Pasarle el self
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * radio ** 2 #Falta: el radio es self.radio

Mi_circulo = Circulo(5)
print("El área del círculo es: mi_circulo.calcular_area()") #Falta: el print esta mal, deberia ser print(f"El tamaño del círculo es: {mi_circulo.calcular_area()}")


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
#Falta: importar el random, y corregir el randint
numero = random.randit(1, 10)
print(f"El número aleatorio generado es: " + numero) #Falta: arreglar el print

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower in vocales: #Falta: .lower() es una funcion por ende tiene que llevar () 
        contador + 1 #Falta: Corregir el contador

print("Número de vocales en la cadena:  {contador}") #Falta: formatear el print

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return #Falta: Corregir el return, repetir_cadena tiene que devolver el resultado

texto = input("Ingrese un texto: ")
repeticiones = input("¿Cuántas veces desea repetir el texto? ") #Falta: pasar a int el input
print(f"El texto repetido es: {repetir_cadena}") #Falta: pasarle por argumento a repetir_cadena el texto y repeticiones

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.

class Personas:
    def __init__(self, nombre, edad, profesion):
        self.nombre= nombre
        self.edad = edad
        self.profecion = profesion
    def datos (self):
            print(f"la persona {self.nombre},{self.edad},{self.profesion}")
    def mayor(self): #Falta: Arreglar la logica del mayor
        if self.edad >= 18:
    print = "mayor de 18"
    else = "menor de 18"

gaspar= Personas ("Gaspar",25,"Profesor")
diego= Personas ("Diego",45, "Desarrollador de software")
pamela= Personas ("Pamela", 36, "Estudiante")
