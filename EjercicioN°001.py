import os 
#Calcular nota final del curso de FP
PU = float (input ('Ingrese nota de la primera unidad: '))
SU = float (input ('Ingrese nota de la segunda unidad: '))
TU = float (input ('Ingrese nota de la tercera unidad: '))
TF = float (input ('Ingrese nota del trabajo final:'))
final=(PU * .20) + (SU * .15) + (TU * .15) + (TF * .50)
if final>20:
  print ("Ingrese notas menores a 20")
else:
  if final<=20:
    print ('El promedio final del curso de Fundamentos de programacion: ',final)
print ()