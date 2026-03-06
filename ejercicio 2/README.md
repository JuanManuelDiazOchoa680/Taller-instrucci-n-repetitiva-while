# Programa en python para un jueguito que te baja vida hasta mocharte jajajjajaajajaja

## Análisis

### Variables de entrada

- Hp = vida del personaje

### Procesamiento

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



## Diseño
![diagrama de flujo](diagrama.png)

## Construcción

Está en el archivo personaje_HP.py
