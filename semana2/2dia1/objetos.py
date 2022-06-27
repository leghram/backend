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


class ObjetoModelo:

    def __init__(self, dato1, dato2):
        self.variable1 = dato1
        self.variable2 = dato2
        #esto edefine que se trata de un permiso privado
        self.__valorPrivado = 23

    def Acceso(self):
        print("Accede a privado por el canal correspondiente ", self.__valorPrivado)




mas = ObjetoModelo(123,543)
mas.Acceso()
print(mas.__valorPrivado)