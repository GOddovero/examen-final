"""
Recuperatorio examen final!
Nombre y Apellido: 
Edad:
DNI:
Email:
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario.
#Resultado esperado: Hola, {NombreUsuario}! Bienvenido!. Siendo NombreUsuario el nombre ingresado por teclado.  
#Cantidad errores: 3
NombreUsuario = input("Ingrese su nombre: )
print("Hola, {NombreUsuario}! Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros. 
#Resultado esperado: El promedio de 4 numeros, si ingreso 5-10-7-8 el promedio deberia imprimir 7,5
#Cantidad errores: 5
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
num3 = input("Ingrese el tercer número: ")

PROMEDIO = num1 + num2 + num3 / 3
print(f"El promedio es: {PROMEDIO}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Salida: Si la calificacion ingresada es mayor o igual que 6: El estudiante ha aprobado, Si no, El estudiante ha reprobado.
#Cantidad de errores: 3

calificacion = input("Ingrese la calificación del estudiante: ")
texto = "El estudiante ha aprobado"
if calificacion <= 6:
    print(texto)
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
for i in range(lista_compras):
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Salida esperada: 78.53975
#Cantidad de errores: 5

class Circulo:
    def init(radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * radio ** 2 #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.

Mi_circulo = Circulo(5)
print("El área del círculo es: " mi_circulo.calcular_area())


#Ejercicio 6: Generar un numero Aleatorio.
#Salida esperada: El número aleatorio generado es: (un numero generado aleatoreamente)
#Cantidad de errores: 3
numero = random.randit(1, 10)
print("El número aleatorio generado es: " + numero)

#Ejercicio 7: Contar Vocales en una Cadena:
#Número de vocales en la cadena:  4
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena
    if letra.lower in vocales:
        contador + 1

print("Número de vocales en la cadena: " contador)

#Ejercicio 8: Funcion para repetir cadenas.
#Salida esperada: Al ingresar como texto Hola y 3 como cantidad de veces a repetir, deberia imprimir: El texto repetido es: HolaHolaHola
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return 

texto = input("Ingrese un texto: ")
repeticiones = input("¿Cuántas veces desea repetir el texto? ")
print(f"El texto repetido es: {repetir_cadena}")

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