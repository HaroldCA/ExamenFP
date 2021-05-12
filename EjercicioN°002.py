import os
#Definir puntos de porfesores 
puntos= int (input ('Ingrese la puntuacion: '))
salario= int (input ('Ingrese el salario minimo: '))
if puntos <50:
  print ("Puntos insuficientes para recibir el bono")
else:
  if puntos<=100:
    bono=(salario * .10)
  else:
    if puntos<=150:
      bono=(salario * .40)
    else:
      bono=(salario * .70)
  print (("Los puntos obtenidos son: "),puntos)
  print (("Te corresponde un bono de:s/."),bono)
print()