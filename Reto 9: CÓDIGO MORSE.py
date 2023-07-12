'''
/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */ '''

#morse={'.-', '-...', '-.-.', '----', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---.--', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'}
#letras={'a','b','c','ch','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'}

morse= dict(a='.-', b='-...', c='-.-.', ch='----', d='-..', e='.', f='..-.', g='--.', h='....', i='..', j='.---', k='-.-', l='.-..', m='--', n='-.', ñ='---.--', o='---', p='.--.', q='--.-', r='.-.', s='...', t='-', u='..-', v='...-', w='.--', x='-..-', y='-.--', z='--..')

palabra='hola'
cadena=' '

for n in palabra:
    for i in morse.keys():
        if n==i:
            cadena = cadena + morse.get(n) + ' '

print(palabra, cadena)