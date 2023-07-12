'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''
def EsAnagrama(palabra,contador):
    if (len(palabra) == contador):
        return True
    else:
        return False

'''
palabra1=input('Escribe primera palabra: ')
palabra2=input('Escribe segunda palabra: ')
'''
palabra1='roma'
palabra2='maro'

palabra3=palabra2
contador = 0

if(palabra1==palabra2 or len(palabra1)!=len(palabra2)):
    print('no son Anagrama')
else:
    for i in palabra1:
        for j in palabra3:
            if([i]==[j]):
                contador += 1

print(EsAnagrama(palabra1,contador))

