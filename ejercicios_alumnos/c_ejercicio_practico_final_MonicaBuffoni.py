"""
Nombre y Apellido: Mónica Marina Buffoni
Edad: 44
DNI:27632290
Email:monicamarinabuffoni@gmail.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
Nombre= input ("Ingrese su nombre"): #Falta: El nombre de la variable tiene que ir en snake_case deberia ser nombre
print("Hola, {Nombre}! Bienvenido!") #Falta: El print no esta formateado


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
#Falta: un numero entero, el enunciado pedia 4 numeros
#Falta: convertir los input a int
num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")
num3 = input("Ingrese el tercer numero: ")
PROMEDIO = num1 + num2 + num3 / 3 #Falta: cambiar el nombre de la variable para que no sea una constante
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = input("Ingrese la calificación del estudiante: ") #Falta:Cambiar el tipo de dato a int
texto = "El estudiante ha aprobado"
if calificacion >= 6:
    print(texto)
else:
    texto= "El estudiante ha reprobado"
print(texto)#Falta: Corregir para que no de dos mensajes de aprobado

#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)

print("Lista de compras:")
for i in range(lista_compras): #Falta: el en el range la funcion len(lista_compras)
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def_init_(radio): #Falta: el self y el __init__ esta mal escrito
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * radio ** 2 #Falta: el radio es self.radio

Mi_circulo = Circulo(5) #Falta: corregir el nombre de la variable
print("El área del círculo es: " mi_circulo.calcular_area()) #Falta: formatear el print con f 


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
numero = random.randit(1, 10) #Falta: importar el random, y corregir el randint
print("El número aleatorio generado es: " + numero) #Falta: Arreglar el print

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena #Falta: los dos puntitos
    if letra.lower in vocales: #Falta: .lower es una funcion, faltan los ()
        contador + 1 #Falta: Corregir el contador

print("Número de vocales en la cadena: " contador) #Falta: Corregir el print

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return #Falta: que la funcion devuelva resultado

texto = input("Ingrese un texto: ")
repeticiones = input("¿Cuántas veces desea repetir el texto? ") #Falta: convertir el input a int
print(f"El texto repetido es: {repetir_cadena}") #Falta: pasarle por parametros texto y repeticiones

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.

#Falta: el ejercicio completo