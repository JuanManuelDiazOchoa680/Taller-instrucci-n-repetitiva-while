#Programa en python para que calcule e imprima en cuántos meses, uniendo los dos capitales, pueden hacer el negocio que desean Juan y Pedro

#libraries
import math

#input

c1=float(input("digite el capital de Pedro: "))
print("")
c2=float(input("digite el capital de Juan: "))
print("")
c3=float(input("digite el capital del negocio: "))
print("")
n1=0
n2=0
if c1+c2<c3:
    "ta bien"
else:
    c3=float(input("no sirve, intenta de nuevo colocar el capital del negocio: "))
    print("")

#processing

if c3>c2+c1:
    while c1<c3:
        c1=c1+0.03*c1
        n1=n1+1
        if c1>=c3:
            break

    while c2<c3:
        c2=c2+0.04*c2
        n2=n2+1
        if c2>=c3:
            break

#output

    print("juan tendra el capital en: " +str(n2)+str(" meses"))
    print("")
    print("pedro tendra el capital en: " +str(n1)+str(" meses"))
    print("")


if n1>n2:
    print("por lo que podran comprar el negocio en: " +str(n1)+str(" meses"))
elif n1==n2:
    print("por lo que podran comprar el negocio en: " +str(n1 or n2)+str(" meses"))
else:
    print("por lo que podran comprar el negocio en: " +str(n2)+str(" meses"))