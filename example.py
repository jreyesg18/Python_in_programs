morse= dict(a='.-', b='-...', c='-.-.', ch='----', d='-..', e='.', f='..-.', g='--.', h='....', i='..', j='.---', k='-.-', l='.-..', m='--', n='-.', ñ='---.--', o='---', p='.--.', q='--.-', r='.-.', s='...', t='-', u='..-', v='...-', w='.--', x='-..-', y='-.--', z='--..')

letras={'a','b','c','ch','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'}

palabra='hola'
cadena=' '

for n in palabra:
    for i in morse.keys():
        if n==i:
            cadena = cadena + morse.get(n)
cadena = cadena + ' '
print(cadena)

