"""
Recuperatorio examen final!
Nombre y Apellido: jonatan gallardo
Edad:35
DNI:34790760
Email:jonatangallardo242@gmail.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario.
#Resultado esperado: Hola, {NombreUsuario}! Bienvenido!. Siendo NombreUsuario el nombre ingresado por teclado.  
#Cantidad errores: 3
nombre_usuario = input("Ingrese su nombre" ) #Falta, las comillas estan mal cerradas dejando los dos puntos fuera.
print(f"Hola, {nombre_usuario}! Bienvenido!")
#errores: 1_la variable no esta en snake_case. 2_falta comillas 3_ formatear print

#Ejercicio 2: Promedio de 4 numeros. 
#Resultado esperado: El promedio de 4 numeros, si ingreso 5-10-7-8 el promedio deberia imprimir 7,5
#Cantidad errores: 5
num1 = int(input("Ingrese el primer número: "))#errores: 1_convertir a enteros. 2_ falta un numero. 3_promedio no esta en snake case
num2 = int(input("Ingrese el segundo número: "))# 4_encerrar nuemero en corchetes. 5_formatear print
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))
promedio = (num1 + num2 + num3 + num4) / 4
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Salida: Si la calificacion ingresada es mayor o igual que 6: El estudiante ha aprobado, Si no, El estudiante ha reprobado.
#Cantidad de errores: 3

calificacion = int(input("Ingrese la calificación del estudiante: "))#HERRORES: 1_poner enteros en calificacion
texto = "El estudiante ha aprobado"
if calificacion >= 6: #2 cambiar flecha a mayor
    print(texto)
else:
    texto= "El estudiante ha reprobado"
    print(texto) #3_tabular print

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
for i in range(len(lista_compras)):# error : 1_colocar len()
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Salida esperada: 78.53975
#Cantidad de errores: 5

class Circulo:
    def __init__(self,radio):# error 1_colocar self 2_ colocar guines bajos al init
        self.radio = radio

    def calcular_area(self):#colocar self en radio
        return 3.14159 * self.radio ** 2 #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.

mi_circulo = Circulo(5)
print("El área del círculo es: " (mi_circulo.calcular_area())) #Falta formatear el print.


#Ejercicio 6: Generar un numero Aleatorio.
#Salida esperada: El número aleatorio generado es: (un numero generado aleatoreamente)
#Cantidad de errores: 3
import random # colocar impor ramdom
numero = random.randint(1, 10) # no es randit sino randint
print("El número aleatorio generado es: ", numero)# colocar coma

#Ejercicio 7: Contar Vocales en una Cadena:
#Número de vocales en la cadena:  4
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:# colocar 2 puntos
    if letra.lower() in vocales:# colocar parentecis al lower()
        contador += 1 # colocar el igual

print("Número de vocales en la cadena: ",contador)# colocar una coma

#Ejercicio 8: Funcion para repetir cadenas.
#Salida esperada: Al ingresar como texto Hola y 3 como cantidad de veces a repetir, deberia imprimir: El texto repetido es: HolaHolaHola
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado# colocar resultado

texto = input("Ingrese un texto: ")
repeticiones = int(input("¿Cuántas veces desea repetir el texto? "))# convertir a enteros
print(f"El texto repetido es: {repetir_cadena(texto,repeticiones)}")# colocar texto ,repeticiones

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.
class Persona:
    def __init__(self, nombre, edad, profecion):
        self.nombre = nombre
        self.edad = edad
        self.profecion = profecion
        
    def imprimir(self):
        print(f"nombre:{self.nombre}, edad:{self.edad}, profecion:{self.profecion} ")
        
    def es_mayor_edad (self):
        if self.edad >= 18:
            return "es mayor de edad"
        else:
            return "es menor de edad"

persona_1= Persona("gaspar", 23, "profesor")
persona_2= Persona("diego", 45, "desarrollador de sofwear")
persona_3= Persona("fermin", 23, "estudiante")
        
persona_1.imprimir()
persona_2.imprimir()
persona_3.imprimir()

print(persona_1.es_mayor_edad())
print(persona_2.es_mayor_edad())
print(persona_3.es_mayor_edad())
        
"""
Salida esperada:
Nombre: Gaspar, Edad: 23, Profesion: Profesor
Nombre: Diego, Edad: 45, Profesion: Desarrollador de Software
Nombre: Fermin, Edad: 16, Profesion: Estudiante
Es mayor de edad
Es mayor de edad
No es mayor de edad (Este varia dependiendo de la tercer persona ingresada)
"""