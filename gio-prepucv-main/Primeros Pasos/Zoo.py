edad = int(input('Digame su edad '))
tipo_de_carnet = input('Digame su tipo de carnet (A para pro, B para noob) ')

if (25 <= edad <= 35 and tipo_de_carnet == 'A') or \
        edad < 10 or\
        (edad >= 65 and tipo_de_carnet == 'B'):
    print('Se te aplica el descuento')
else:
    print('No se te aplica el descuento')
 