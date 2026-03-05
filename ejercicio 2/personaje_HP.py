# Programa para una parte de un videojuego(no se como describrlo)

#libraries
import random

#input

print("")
print("     Cuidado con el jefe      ")
print("")

c=random.randint(1, 50)
Hp=int(input("digita el valor de tu vida que es 50: "))

#processing and output

while True:
    print("el jefe te bajo: " +str(c))
    Hp=Hp-c
    c=random.randint(1, 50)
    if(Hp<0):
        break
print("Perdiste")

