'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

def Es_primo(num):
    for n in range(2,num):
        if(num%n == 0):
            print(num,'no es primo')
            return False

    print(num, 'es primo')
    return True

for n in range(1, 100):
    Es_primo(n)