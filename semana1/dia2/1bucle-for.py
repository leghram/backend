from unicodedata import bidirectional


numeros = [23,23,3,23,43,5,65]

for numero in numeros:
    print(numero)

frase = 'esto es una frase o cadena de texto'

contador =0
for caracter in frase:
    print (caracter)
    if( caracter == 'o'):
        contador+=1
        
print ("hay {} veces la letra o".format(contador))


print ("__________")


for num in range(2,15,3):
    print (num)



numPares = 0
numMul3 = 0
numeros = [10,30,12,17,24,67]

for numero in numeros:
    if(numero%2 ==0):
        numPares+=1
    if(numero%3 ==0):
        numMul3+=1

print ("hay {} numeros pares".format(numPares))
print("hay {} numeros multiplos de 3".format(numMul3))
print("___________")

for num in range(40):
    print(num)
    if num==15:
        break

print("___________")

for num in range(40):
    if num==15:
        continue
    print(num)