# Prorgrama para saber si dependiendo de la altura de donde cae la pelota, determinar hasta donde llega a 1/5 de la altura inicial y en que rebote

#libraries
import math


print("")
print("      PELOTA MOMENT      ")
print("")

h=int(input("Digite la altura en donde sera dejada caer la pelota: "))
l=h/5
n=0


while True:
    h=h-(h*0.10)
    n=n+1
    print("rebote, llegó a subir a " +str(h)+str(" metros"))
    print("")
    if(h<l):
        break


print("")
print("      RESULTADOS      ")
print("")
print("la pelota llego a menos de 1/5 de la altura colocada en el rebote numero: " +str(n))
print("")