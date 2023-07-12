import random

def Adivinar(num):
    eleccion=0
    while(eleccion != num):
        eleccion = int(input('Elige un numero: '))
        if eleccion==num:
            return 1
            break


num= random.randrange(0,50)

if(Adivinar(num)==1):
    print('Adivinaste')