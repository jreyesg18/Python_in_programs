'''
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
'''


palabra = 'Hola, mi nombre es reyes. Mi nombre completo es reyes'
palabra = palabra.lower()
palabra = palabra.split(' ')

palabra2 = palabra

for n in palabra:
    print(n)
    contador=-1
    for j in palabra:
        if n==j:
            contador+=1
    print('se repite: ',contador)
    j=0

