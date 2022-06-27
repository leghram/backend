print("OBJETOS")


class Molde:
    altura=2
    color='azul'

    def saludar(self):
        print("hol es funcion")

obj1 = Molde()

print(obj1.color)
obj1.saludar()


class MoldeCompleto:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluda(self):
        print("hola ", self.nombre)


obj2 = MoldeCompleto('MIGUEL',23)

print(obj2.nombre)







