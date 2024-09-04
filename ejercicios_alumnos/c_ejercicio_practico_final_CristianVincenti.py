"""
Nombre y Apellido: CRISTIAN VINCENTI
Edad: 48
DNI: 24.878.390
Correo electrónico: cristianvincenti@gmail.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario.
#Cantidad errores: 3
nombre_usuario  =  input (" Ingrese  su  nombre: ")
print ( f"¡Hola, {nombre_usuario}! ¡Bienvenido!" )


#Ejercicio 2: Promedio de 4 números.
#Cantidad errores: 5
num1  =  int(input ( "Ingrese el primer número: " ))
num2  =  int(input ( "Ingrese el segundo número: " ))
num3  =  int( input ( "Ingrese el tercer número: " ))
num4  =  int(input ( "Ingrese el cuarto número: " ))
PROMEDIO  =  float(num1  +  num2  +  num3 + num4) /  4 #Falta cambiar el nombre de la variable, en este momento promedio es una Constante ya que esta en mayusculas.
print ( f"El promedio es: { PROMEDIO } " )


#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion  = int(input ( "Ingrese la calificación del estudiante: "))
texto = "El alumno ha aprobado"
if calificacion  >= 6:
    print ( texto )
else:
    print ("El estudiante ha reprobado")


#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ").lower()
    if item == 'salir':
        break
    lista_compras.append(item)

print("Lista de compras:")
for i in range(len(lista_compras)):
    print("- " + lista_compras[i])



#Ejercicio 5: Clase Círculo.
#Cantidad de errores: 5

class  Circulo:
    def __init__(self)-> None:
        self.radio = int(input(" Ingrese el alto: ")) #No es el alto, es el radio, esta mal el texto
    pass

    def  calcular_area ( self ):
        area=  self.radio* 3.14159 **  2 #Esta mal la formula del area, es pi(3.14159) por el radio al cuadrado
        return area   #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.

#print ( f"El área del círculo es: "  {calcular_area})
    def caracterisca (self): #No hacia falta crear otro metodo para mostrar el area, si pones print(mi_circulo.calcular_area()) lo muestra
        print ( f"El área del círculo es:   {self.calcular_area()}")

mi_circulo =  Circulo()
mi_circulo.caracterisca()

#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
import random

numero  =  random.randint (1,10)
print (f"El número aleatorio generado es:  {numero}" )


#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower() in vocales:
        contador += 1

print(f"Número de vocales en la cadena:  {contador}")


#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena: str, veces: int):
    resultado = cadena * veces
    return resultado

texto = input("Ingrese un texto: ")
repeticiones = int(input("¿Cuántas veces desea repetir el texto? "))
print(f"El texto repetido es: {repetir_cadena(texto, repeticiones)}")



#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23 años, Profesor.
# Diego, 45 años, desarrollador de software.
# Tu nombre, tu edad, tu profesión.
# Crea métodos para imprimir el nombre, la edad y la profesión de cada persona.
# Crea un método para saber si la persona es mayor o menor de edad.

class Persona:
    def __init__(self, nombre: str, edad: int, profesion: str, ) -> None: #Excelente uso de decoradores
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        pass
    

    def mayor(self):
        if self.edad > 18: #Falto el =, deberia ser >= 18 o bien > 17 ya que con 18 años sos mayor de edad.
            print(f" {self.nombre} es mayor de edad")
        else:
            print(" Es menor de edad")
    
datos_personales = Persona("Gaspar", 23, "Profesor")
datos_personales1= Persona("Diego", 45, "desarrollador de software")
datos_personales2= Persona("Cristian", 48, "Adminitrativo")
datos_personales.mayor()
datos_personales1.mayor()
datos_personales2.mayor()