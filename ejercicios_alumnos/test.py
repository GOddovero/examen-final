class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        pass

    def mostrar_nombre(self):
        print(f"El nombre de la persona ingresada es: {self.nombre}")
        return
    
    def mostrar_edad(self):
        print(f"La edad de la persona ingresada es: {self.edad}")
        return
    
    def mostrar_profesion(self):
        print(f"La profesion de la persona ingresada es: {self.profesion}")
        return
    
    def mostrar_edades(self):
        if self.edad >= 18:
            print("La persona ingresada es mayor de edad")
        else:
            print("La persona ingresada es menor de edad")
        return

personas = Persona("Gaspar", 23, "Profesor")
personas.mostrar_nombre()
personas.mostrar_edad()
personas.mostrar_profesion()
personas.mostrar_edades()

persona2 = Persona ("Diego",45,"Desarrollador de sofwear")
persona2.mostrar_nombre()
persona2.mostrar_edad()
persona2.mostrar_profesion()
persona2.mostrar_edades()

persona3 = Persona ("Carlos",17,"Empleado")
persona3.mostrar_nombre()
persona3.mostrar_edad()
persona3.mostrar_profesion()
persona3.mostrar_edades()
