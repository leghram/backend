from cgitb import text
from operator import indexOf
from camelcase import CamelCase

print("2 LIBRERIAS")

camel = CamelCase()
texto = "qye pasa si no es cierto"

resul = camel.hump(texto);

print(resul)
print("_____")


palabras = []
porcion = ""
posicion =0
texto = texto + " "
mm=""
for a in texto:
    if (texto[posicion] == " "):
        mm=mm+porcion[0].upper() + porcion[1:] + " "
        porcion=""
        posicion+=1
        continue
    porcion = porcion + texto[posicion]
    posicion+=1

mm = mm[0:-1]

print(palabras)
print()
print(mm)
