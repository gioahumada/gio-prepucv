import random

numero = random.randint(1, 10)
adivinanza = int(input('Dime un numero de 1 al 10 para adivinarlo: '))
if adivinanza == numero:
    print('Felicidades')

if adivinanza > 10:
    print('Fuiste de rosca')
if adivinanza < 1:
    print('Un poco bajo')
