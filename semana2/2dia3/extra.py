from asyncio import CancelledError
from audioop import reverse
from difflib import Match
from itertools import count
import math
from random import Random

from pkg_resources import get_supported_platform


grupo = ['letras','asd tesxto','mas ocntenido','agregando','y no mas']

print(grupo[-2:-1])


grupo.insert(1,"mas texto")
grupo.extend("es real")

print(grupo)
print(grupo.index(" "))

print(grupo.__len__())
print(len(grupo))
print("letras" in grupo)
print(grupo.count("y no mas"))


dic = {
    'nomre': "miguel",
    'dni':344,
    43:"hola",
}


print(dic)



grupo = ['letras','asd tesxto','mas ocntenido','agregando','y no mas']


for i in grupo:
    print(grupo.index(i))



numero = Random()

print(numero)

cadena = """
    D:/nombre/trabajos
"""

print(cadena)

masa = 212
masa2 =''
for letra in str(masa):
    masa2 = letra + masa2



if(str(masa) == masa2):
    print("son capicuas")
else:
    print("nel man")

