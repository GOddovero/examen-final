"""
Nombre y Apellido:jonatan gallardo 
Edad:
DNI:34790760
Email:jonathangallrdo@gmail.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
NombreUsuario = input("Ingrese su nombre:") #Falta: el nombre de la variable no esta en snake_case, deberia ser nombre_usuario
print(f"Hola, {NombreUsuario}! Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("ingrese el cuarto numero:"))
PROMEDIO = num1 + num2 + num3 + num4 / 4 #Falta: Promedio no es una constante ya que cambia dependiendo de los numeros que el usuario ingresa, deberia ser promedio.
print(f"El promedio es: {PROMEDIO}")
#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = int(input("Ingrese la calificación del estudiante: "))
texto = "El estudiante ha aprobado"
if calificacion <= 6:#Falta: Esta al reves el simbolo, si el alumno saca menos de 6 aprueba, deberia ser al reves. 
    print(texto)
else:
    texto= "El estudiante ha reprobado"
print(texto) #Falta, si el usuario aprueba se imprime dos veces el mensaje de "El estudiante ha aprobado"

#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)

print("Lista de compras:")
for i in range(5) (len(lista_compras)):
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def init(radio): #Falta, no se paso el self en los argumentos y el init esta mal declarado, deberia ser def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * radio ** 2 #Falta, aca hay que pasarle self.radio no radio

Mi_circulo = Circulo(5)
print("El área del círculo es: " mi_circulo.calcular_area()) #Falta, esta mal estructurado el print. Falta la f al principio y arreglar las comillas.


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
import random
numero = random.randit(1, 10) #Falta: el metodo correcto es randint
print("El número aleatorio generado es: " + numero) #Falta: print no te deja concatenar texto y numeros, por eso hay que usar str() una coma o bien el formateo con f.

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower() in vocales:
        contador = + 1 #Falta: el contador esta al reves, no almacena sino que asigna el 1 en cada iteracion. deberia ser contador +=1

print("Número de vocales en la cadena: " (contador)) #Falta: print no te deja concatenar texto y numeros, por eso hay que usar str() una coma o bien el formateo con f.

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return #Falta, no retorna el resultado

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

#Falta el ejercicio completo.