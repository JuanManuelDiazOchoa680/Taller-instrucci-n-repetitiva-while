# Programa para una parte de un videojuego(no se como describrlo)

#libraries
import random

#input

print("")
print("     Cuidado con el jefe      ")
print("")

c=random.randint(1, 20)
Hp=50
j=40
a=input("ataca: ")
a=random.randint(4, 20)

#processing and output

while True:
    print("el jefe te bajo: " +str(c))
    print("le bajaste al jefe: " +str(a))
    print("")
    Hp=Hp-c
    j=j-a
    print("tienes: " +str(Hp)+str(" de vida"))
    print("el jefe tiene: " +str(j)+str(" de vida"))
    print("")
    if(Hp<=0):
        print("perdiste")
        break
    if(j<=0):
        print("ganaste")
        break
    a=input("!ataca de nuevo¡: ")
    print("")
    a=random.randint(1, 20)
    c=random.randint(1, 20)

