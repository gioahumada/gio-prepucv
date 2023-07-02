import random
import os

VIDA_PIKACHU_INICIAL = 80
VIDA_SQUIRTEL_INICIAL = 90

vida_pikachu = VIDA_PIKACHU_INICIAL
vida_squirtel = VIDA_SQUIRTEL_INICIAL


while vida_pikachu > 0 and vida_squirtel > 0:
    #Se desenvuelven los turnos de combate
    os.system ("cls") 
    print('-'*40)
    print('Turno de Pikachu')
    print('-'*40)
    input('\n Enter para continuar...')
    os.system ("cls") 
    ataque_pikachu = random.randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print('-'*40)
        print('Pikachu ataca con bola voltio')
        print('-'*40)
        vida_squirtel -= 10
    else:
        print('-'*40)
        print('Pikachu ataca con Onda Trueno')
        print('-'*40)
        vida_squirtel -= 11

    input('\n Enter para continuar...')
    os.system ("cls") 
    print('\n La vida de Pikachu es: [{}] {} \n La vida de Squirtle es: [{}] {}'.format(int(vida_pikachu/10)* '#', vida_pikachu, int(vida_squirtel/10)* '#', vida_squirtel))
    input('\n*Enter* para continuar...')
    os.system ("cls") 

    
    #Turno Squirtle
    print('-'*40)
    print('Ataque Squirtle')
    print('-'*40)
    input('\n*Enter* para continuar...')
    os.system ("cls") 
    
    ataque_squirtle = None
    while ataque_squirtle != 'P' and ataque_squirtle != 'A' and ataque_squirtle != 'B':
        ataque_squirtle = input('Que ataque deseas realizar? [P]lacaje , Pistola [A]gua , [B]urbuja \n')
    if ataque_squirtle == 'P':
        print('-'*40)
        print('Squirtle ataca con Placaje')
        print('-'*40)
        vida_pikachu -= 10
    elif ataque_squirtle == 'A':
        print('-'*40)
        print('Squirtle ataca con Pistola de Agua')
        print('-'*40)
        vida_pikachu -= 12
    elif ataque_squirtle == 'B':
        print('-'*40)
        print('Squirtle ataca con Burbuja')
        print('-'*40)
        vida_pikachu -= 9
    print('\n La vida de Pikachu es: [{}] {} \n La vida de Squirtle es: [{}] {}'.format(int(vida_pikachu/10)* '#', vida_pikachu, int(vida_squirtel/10)* '#', vida_squirtel))
    input('\n Enter para continuar...')

if vida_pikachu > vida_squirtel:
    os.system ("cls") 
    print('-'*40)
    print('Pikachu a ganado')
    print('-'*40)
else:
    os.system ("cls") 
    print('-'*40)
    print('Squirtle a ganado')
    print('-'*40)
