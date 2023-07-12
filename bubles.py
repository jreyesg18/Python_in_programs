def RaizCuadrada(a,b):
    print(round(((a+b)**0.5),2))
def Division(a,b):
    print(a/b)
def Multipl(a,b):
    print((a*b)/2.5)

a=4
b=2
eleccion=0
cont = ' '

while(cont != 'salir'):

    eleccion = int(input(' 1.Raiz cuadrada\n 2. Division\n 3. ( A * B ) / 2.5\n Elige tu opcion: ' ))

    if eleccion==1:
        RaizCuadrada(a,b)
    elif eleccion == 2:
        Division(a,b)
    else:
        Multipl(a,b)

    elegir = input('escriba: ')
    cont = cont.replace(cont, elegir)
