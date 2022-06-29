

print ("DIA 2 HERENCIA")

class Usuario:
    def __init__(self,nom, ape):
        self.nombre = nom
        self.apellido = ape

class Alumno(Usuario):
    def __init__(self, nom, ape, sec):
        super().__init__(nom, ape)
        self.seccion = sec

    def info(self):
        return {
            'nombre':self.nombre,
            'apellido':self.apellido,
            'seccion':self.seccion 
        }

Alu1 = Alumno('Miguel', 'par', 4)
Us1 = Usuario('oscar','asdf')


veamos = Alu1.info();

print(veamos)

