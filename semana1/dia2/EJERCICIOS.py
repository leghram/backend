
print("EJERCICIOS SEMANA 2 / RETO DE LA SEMANA")

# ejemplo
# Para evitar que en cada impresion se ejecute una nueva linea, se puede agregar el parametro end y este indicara como queremos que actue al finalizar la linea
for numero in range(5):
     print(numero, end="")
print()
print("_______________")

#****************************************
# EJERCICIO 1
# Escriba el codigo que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****

altura = int(input("ingresa la altura : "))
largo = int(input("ingresa el largo : "))

for a in range(altura):
     for b in range(largo):
          print("*",end="")
     print("")







# EJERCICIO 2
# Escribir el codigo que el usuario le ingrese el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****

grosor = int(input("ingresa el ancho : "))
costado=5
ancho = grosor + 2*costado
fila=0

for a in range(14):
     print(" "*costado + "*"*grosor + " "*costado)

     if fila<4:
          costado-=1
          grosor+=2
     elif fila>=4 and fila <=8:
          pass
     else:
          costado+=1
          grosor-=2
     fila+=1













# EJERCICIO 3
# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *

lado = int(input("Ingresa el lado del triangulo : "))

for a in range(lado):
     print("*"*lado)
     lado-=1









# EJERCICIO 4
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12



numero = int(input("ingresa un numero : "))
while numero != 1:
     print(numero)
     if(numero%2 == 0):
          numero= numero/2
     else:
          numero = numero*3 + 1






# EJERCICIO 5
# si el texto de ingreso es:
texto = "hola alumnos buenas noches ya se viene el break"
# entonces el texto resultado debera ser:
resultado_final = ["Hola", "Alumnos", "Buenas", "Noches", "Ya", "Se"]
# Hacer el codigo para ello

frase = input("ingrese un texto : ")
frase = frase + " "
resultado = []
posicion = 0
contador = 0
for a in frase:
     if a == " ":
          resultado.append(frase[posicion:contador])
          posicion = contador + 1
     contador+=1
print(resultado)








# EJERCICIO 6
# ingresar numeros hasta que ese numero sea adivinado
numero_adivinar = 10
# 5 => 'el numero es mayor que ese'
# 13 => 'el numero es menor que ese'
# 10 => 'felicidades adivinaste el numero'

numero = 0
while numero != numero_adivinar:
     numero = int(input("Ingresa un numero : "))
     if(numero > numero_adivinar):
          print("El numero es menor que ese que ingresaste")
     elif numero < numero_adivinar:
          print("El numero es mayor que ese que ingresaste")
     else:
          print("felicidades, adivinaste")






# EJERCICIO 7
# dado los siguientes numeros:
numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
# indicar cuantos de ellos son multiplos de 3 y de 5 , ademas si hay un multiplo de 3 y de 5 no contabilizarlos
# multiplos de 3: 3 , multiplos de 5: 1
mul3=0
mul5=0
mul3y5=0
for numero in numeros :
     if numero % 3 == 0:
          mul3+=1
     if numero % 5 ==0:
          mul5+=1
     if numero%3 ==0 and numero %5 ==0:
          mul3y5+=1

print("multiplos de 3 : ", mul3)
print("Multiplos de 5 : ", mul5)
print("Multiplos de 3 y de 5 : ", mul3y5)



