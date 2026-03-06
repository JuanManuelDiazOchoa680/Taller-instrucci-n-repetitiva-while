#

#libraries
import random

#input

cn=random.randint(1, 100)
un = 0
n=0
#processing and output

while un != cn:
    un = int(input("Adivina el número (1-100): "))
    n=n+1

    if un < cn :
        print("mas alto: ")
    elif(un>cn):
        print("mas bajo: ")
    else:
        break

print("LO CONSEGUISTE EN: " +str(n)+str(" intentos"))


