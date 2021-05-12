import os
#Defirnir que vacuna te corresponde segun la edad
edad= int (input ('Ingresa tu edad: '))
if edad>=70:
  vacuna=("C")
else:
  if edad<16:
    vacuna=("A")
  else:
    sexo= int (input ('Ingresa el sexo: 1 = mujer o 2 = Hombre: '))
    if sexo ==1:
      vacuna=("B")  
    else:
      if sexo==2:
        vacuna=("A")
      else:
        print ("Ingresa un sexo correcto")
print (("Te corresponde la vacuna: "),vacuna)
print()