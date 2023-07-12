'''
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
'''

decimal = 6  # 110
final = 0
cont = 1

while decimal > 0:
    final = final + (decimal % 2) * cont
    decimal = int(decimal / 2)
    cont = cont * 10

print(final)
