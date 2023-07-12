
Usuario= int(input('1.tijera,2.papel.3.roca: '))
PC= int(input('1.tijera,2.papel.3.roca: '))

if Usuario == 1:
    eleccionusu = 'tijera'
if Usuario == 2:
    eleccionusu = 'papel'
if Usuario == 3:
    eleccionusu = 'roca'

if PC == 1:
    eleccionPc='tijera'
if PC == 2:
    eleccionPc = 'papel'
if PC == 3:
    eleccionPc = 'roca'

if eleccionusu =='tijera' and eleccionPc=='tijera':
    print('empate')
if eleccionusu =='tijera' and eleccionPc=='papel':
    print('Gano usuario')
if eleccionusu == 'tijera' and eleccionPc == 'roca':
    print('Gano PC')

if eleccionusu == 'papel' and eleccionPc == 'tijera':
    print('Gano PC')
if eleccionusu == 'papel' and eleccionPc == 'papel':
    print('empate')
if eleccionusu == 'papel' and eleccionPc == 'roca':
    print('Gano usuario')

if eleccionusu == 'roca' and eleccionPc == 'tijera':
    print('Gano usuario')
if eleccionusu == 'roca' and eleccionPc == 'papel':
    print('Gano PC')
if eleccionusu == 'roca' and eleccionPc == 'roca':
    print('empate')
