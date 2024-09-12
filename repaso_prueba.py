"""#Declarando la clase Perro

class Perro:
    def __init__(self, nombre, ladrido, color):
        self.nombre = nombre
        self.ladrido = ladrido
        self.color = color
        pass
    def cambiar_color(self):
        nuevo_color = input("Ingrese el nuevo color del perro: ")
        self.color = nuevo_color
    def caracteristicas(self):
        print(f"El perro se llama {self.nombre} y ladra {self.ladrido} y el color del perro es {self.color}")
nombre = input("Ingrese el nombre del perro: ")
ladrido = input("Ingrese el ladrido del perro: ")
dogo = Perro(nombre, ladrido, "Blanco")

dogo.caracteristicas()

dogo.cambiar_color()
dogo.caracteristicas()

frutas = ["manzana", "pera", "uva", "naranja"]
for fruta in frutas:
    print(fruta)

"""
