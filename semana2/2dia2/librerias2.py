from configparser import DuplicateSectionError
from operator import truediv
from camelcase import CamelCase

print("LIBRERIAS SEGUNDA PARTE ")

objCamel = CamelCase()

texto = "Este es un texto de prueba"

converCamel = objCamel.hump(texto)


print("INGRESE UN TEXTO")
texto = input()
stop = False

while(stop!=True):
    print("1: Mostrar sus 2 primeras letras")
    print("2: Mostrar sus 3 primeras letras")
    print("3: Mostrar sus 2 ultimas letras")
    print("4: Mostrar su ultima letra")
    print("5: SALIR")
    try:
        opcion = int(input("ingresa una opcion : "))
    except:
        print("respuesta : opcion invalida")
        continue
    if(opcion==1):
        print("Respuesta : "+texto[0:2])
    elif(opcion==2):
        print("Respuesta : "+texto[0:3])
    elif(opcion==3):
        print("Respuesta : "+texto[-2]+ texto[-1])
    elif(opcion==4):
        print("Respuesta : "+texto[-1])
    elif(opcion==5):
        stop=True
    else:
        print("Respuesta : opcion invalida")






















