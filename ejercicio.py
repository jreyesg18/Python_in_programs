# Factorial
cont='sal'
while(cont != 'salir'):

    eleccion=input('escriba: ')
    cont= cont.replace(cont, eleccion)



def factorial(x):
    total = 1
    for n in range(1, x + 1):
        total = n * total
    return total

x = 10
print(factorial(x))