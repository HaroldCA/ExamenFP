import os
#Definir las operaciones aritmeticas
a = int (input ('Ingrese un numero: '))
b = int (input ('Ingrese el otro numero: '))
print ("1 = +")
print ("2 = -")
print ("3 = *")
print ("4 = /")
print ("5 = ^")
x= int (input("Elige un a opcion: "))
if x ==1:
  print (("La suma de"),a,("+"),b,("="),a+b)
if x ==2:
  print (("La resta de"),a,("-"),b,("="),a-b)
if x ==3:
  print (("La multiplicacion de"),a,("*"),b,("="),a*b)
if x ==4:
  print (("La division de"),a,("/"),b,("="),a/b)
if x ==5:
  print (("La potenciacion de"),a,("^"),b,("="),a**b)
print ()