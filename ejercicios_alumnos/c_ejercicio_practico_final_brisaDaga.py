"""
Nombre y Apellido: Brisa Daga
Edad: 21
DNI: 44961358
Email: briaanes@gmail.com
"""
import funciones as fp
import funciones_mias as fm
#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
nombreusuario = input("Ingrese su nombre: ")
print(f"Hola, {nombreusuario} ! Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
num1 = fp.ingresar_numero("Ingrese el primer número: ")
num2 = fp.ingresar_numero("Ingrese el segundo número: ")
num3 = fp.ingresar_numero("Ingrese el tercer número: ")
num4 = fp.ingresar_numero("Ingrese el tercer número: ") #Esta mal el texto

promedio = num1 + num2 + num3 + num4 / 3 #El promedio da mal, falta cambiar el 3 por un 4 en la division.
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = fp.ingresar_numero("Ingrese la calificación del estudiante: ")

if calificacion >= 6:
    print(f"El estudiante ha aprobado con {calificacion}")
if calificacion <= 6: #Esta mal la logica, no hace falta dos if ya que si el usuario saca 6 se comprueban ambas. Va un else.
    print(f"El estudiante ha reprobado con {calificacion}")



#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []
while True:
    item = input("Ingrese un artículo para agregar a la lista o salir para terminar: ")
    if item == "salir" :
        print(f"Su lista de compras es {lista_compras}")
        break
    lista_compras.append(item)


print(f"Su lista de compras es {lista_compras}")
for item in lista_compras: #Falta: El ejercicio funciona perfectamente pero habia que usar el range, con el len para devolver el largo de la lista
    print(f"{lista_compras}")



#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def __init__(self , radio):
        radio = fp.ingresar_numero("Ingrese el radio: ")
        area = 0
        self.radio = radio
        self.area = area

    def calcular_area(self):
         self.area = (3.14159 * self.radio) ** 2 #Esta mal la formula del area, no hace falta pasarle un self.area se puede usar una variable local.
         print(f"{self.area}")

mi_circulo = Circulo(5)
mi_circulo.calcular_area()




#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
import random
numero = random.randint(1, 10)
print(f"El número aleatorio generado es: {numero} ")

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena: 
    if letra  in vocales: #Falta el .lower() si cambias la cadena y una vocal es mayuscula no la tendrá en cuenta.
        contador  += 1 

print(f"Número de vocales en la cadena: {contador}") 

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
texto = input("Ingrese un texto: ")
veces = fp.ingresar_numero("¿Cuántas veces desea repetir el texto? ")
def repetir_cadena(cadena, veces): #No hay que pasarle cadena por parametro, hay que pasarle el texto
    veces = veces
    cadena = texto * veces
    print(f"El texto repetido es: {texto} y la cantidad de veces es {veces}")
    return cadena #

repetir_cadena(veces) #Falta un parametro, hay que pasarle el texto y poner la funcion en un print para que muestre el texto repetido
repetir_cadena(cadena)

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.
class Mi_perona:
    def __init__(self,nombre,edad,profesion) -> None:
        self.nombre= nombre
        self.edad = edad
        self.profesion = profesion
        pass
    def mayor_de_edad(self):
        if self.edad >= 18:
            print("Eres mayor")
        if self.edad < 18:
            print("Eres menor de edad") 
    def datos_completos(self):
        print(f"{self.nombre}, {self.edad},{self.profesion}")


yo = Mi_perona("Diego",44,"programador")
yo.mayor_de_edad()
yo.datos_completos()
yo2 = Mi_perona("Brisa",21,"programadora")
yo2.mayor_de_edad()
yo2.datos_completos()
yo3= Mi_perona("Señor X",200,"No se sabe")
yo3.mayor_de_edad()
yo3.datos_completos()