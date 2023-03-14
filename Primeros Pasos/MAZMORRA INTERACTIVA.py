import random

# Datos #
nombre_jugador = ''
edad_jugador = 18
edad_nueva = random.randint(3,8)


# Columnas de Texto #
txt1 = 'Introduzca su nombre de jugador: '
txt2 = 'Introduzca la edad del personaje: '
txt3 = 'Entrando en un proceso de conexion con otro mundo...'
txterror = 'Toma atencion de lo que contestas...'
txt5 = 'Digita los años que adelantaste...'
txt6 = '¿Deseas llevar la Aspiradora de liquidos de tu casa?'
txt7 = 'Deseas empujar la olla [A] | Llenarla de Tierra [B]'
txt8 = 'Fin'

opc = '[OPCION (A) - Si] | [OPCION (B) - No]'
opc2 = ''
opc3 = ''

# Codigo #

nombre_jugador = str(input('-' * len(txt1) + '\n' + txt1 + '\n' + '-' * len(txt1) + '\n'))
edad_jugador = int(input('-' * len(txt2) + '\n' + txt2 + '\n' + '-' * len(txt2) + '\n'))

txt4 = '¿Deberia ' + nombre_jugador + ' tocar la olla?'

print('\n'*30)

print('-' * len(txt3) + '\n' + txt3 + '\n' + '-' * len(txt3) + '\n')
input('Presione *Enter* para continuar... \n')
print('\n'*30)
#Cadena de texto#
print('En un lejano oeste, muy, pero muy lejos de aqui vivia ' + nombre_jugador)
print('Un Joven agricultor que trabajaba de 7:30AM hasta las 9:00PM todos los dias de su vida.')
print('Desde los ' + str(edad_jugador - 3) + ' que deseaba dejar su arduo trabajo para profesionalizarse... \n')
input('Presione *Enter* para continuar... \n')
print('\n'*30)
print('En su cumpleaños numero ' + str(edad_jugador) + ' paso la tarde junto a sus mejores amigos.')
print('En una ida al bosque, ' + nombre_jugador + ' junto con sus amigos, caminaron por lugares que no debian acceder...')
print('Ellos siguieron, encontrandose con una olla con un liquido purpura, que raramente, emitia una palpitante luz... \n')
input('Presione *Enter* para continuar... \n')
print('\n'*30)

print('Sus amigos asustados, huyeron, pero ' + nombre_jugador + ' se quedo ahi analizando que era aquello que relucia entre')
print('la oscuridad del bosque.\n')
print('-' * len(txt4) + '\n' + txt4 + '\n' + '-' * len(txt4) + '\n')

olla_tocar = input(opc + '\n')
if olla_tocar == 'A':
    print(nombre_jugador + ' toco la olla... \n')
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)

    print('El efecto que a tenido en ' + nombre_jugador + ' el tocar el misterioso liquido a hecho que viaje a una')
    print('dimension desconocida, muy similar al mundo donde vivia, pero con avances tecnologicos que ' + nombre_jugador)
    print('no conocia... \n')
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)

    print('En el camino, se encuentra con un ciudadano...\n')
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)

    print('[{}] ¿Donde estoy?'.format(nombre_jugador))
    print('[{}] ¿Como donde estoy?'.format('Desconocido'))
    print('[{}] ¡No se como llegue aqui!'.format(nombre_jugador))
    print('[{}] Jaaaaaa, ¡otro mas! Mira chico... Hay una forma de escapar de aqui'.format('Desconocido'))
    print('[{}] ¡¿COMO?!'.format(nombre_jugador))
    print('[{}] Si mira... Deja que te explico... \n'.format('Desconocido'))
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)

    print('[{}] Este es un pueblo donde la gente que llega accede al poder de estar {} años '.format('Desconocido',edad_nueva))
    print('adelantado')
    print('[{}] ¿Como es eso?'.format(nombre_jugador))
    print('[{}] Mira por ejemplo, ¿Cuantos años tienes?'.format('Desconocido'))
    print('[{}] {} años.'.format(nombre_jugador, edad_jugador))
    print('[{}] Entonces, aqui deberias tener {}'.format('Desconocido', int(edad_jugador+edad_nueva)))
    print('[{}] ¡Wow! Pero, ahora... ¿Como escapo de aqui? \n'.format(nombre_jugador))
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)
    calculo = edad_jugador + edad_nueva

    print('[{}] Para escapar de aqui primero debes calcular cuantos años has adelantado en el tiempo. \n '
          'Cuando lo tengas, solo gritalo lo tan fuerte puedas. \n'.format('Desconocido'))

    adivinanza = int(input('-' * len(txt5) + '\n' + txt5 + '\n' + '-' * len(txt5) + '\n'))
    if adivinanza == edad_jugador-calculo: #Esto es inecesario, pero era para realizar una operacion arismetica
        print('\n ¡' + nombre_jugador + ' Grita su edad! \n')
        print('Escapas del lugar.')
    else:
        print('\n Eres un fracaso...')
# -------------- #
elif olla_tocar == 'B':
    print('\n' + nombre_jugador + ' no toco la olla... \n')
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)

    print(nombre_jugador + ' sigue a sus amigos...')
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)

    print(nombre_jugador + ' les pregunta a ellos porque no fueron... \n')
    print('[{}] ¿Chicos, que ocurre?'.format(nombre_jugador))
    print('[{}] ¿Acaso no sabes?'.format('Amigos'))
    print('[{}] ¿Que cosa?'.format(nombre_jugador))
    print('[{}] La famosa olla morada, ¿Nunca has oido de ella?'.format('Amigos'))
    print('[{}] Mmm.... no, la verdad. \n '.format(nombre_jugador))
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)

    print('[{}] ¡¡¡Aquella olla, es la que a hecho desaparecer mucha gente!!'.format('Amigos'))
    print('[{}] Wow'.format(nombre_jugador))
    print('[{}] ¡Es nuestra mision eliminarla de aca!'.format('Amigos'))
    print('[{}] ¡Los acompañare! \n '.format(nombre_jugador))
    print(nombre_jugador + ' va hasta su casa a buscar materiales para realizar la hazaña... \n')
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)

    aspiradora = False
    opcion = input('-' * len(txt6) + '\n' + txt6 + '\n' + opc + '\n' + '-' * len(txt6) + '\n')

    if opcion == 'A':
        print('Llevas la aspiradora... \n')
        input('Presione *Enter* para continuar... \n')
        aspiradora = True
    else:
        print('No llevas la aspiradora... \n')
        input('Presione *Enter* para continuar... \n')

    print('\n' * 30)
    print(nombre_jugador + ' Llega con sus amigos al lugar...\n')
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)

    print('[{}] ¿Chicos, que hacemos?'.format(nombre_jugador))
    print('[{}] Acabar con esto. \n'.format('Amigos'))
    input('Presione *Enter* para continuar... \n')
    print('\n' * 30)

    eleccion = input('-' * len(txt7) + '\n' + txt7 + '\n' + '-' * len(txt7) + '\n')

    if eleccion == 'A' and aspiradora == True:
        print('\n Empujaste la Olla, con tu aspiradora limpias el liquido.')
        print('-' * len(txt8) + '\n' + txt8 + '\n' + '-' * len(txt8) + '\n')
    elif eleccion == 'A':
        print('\n Empujaste la Olla, ahora quedo todo disperso. \n')
        print('-' * len(txt8) + '\n' + txt8 + '\n' + '-' * len(txt8) + '\n')
    elif eleccion == 'B':
        print('\n Tapaste la olla con tierra.')
        print('-' * len(txt8) + '\n' + txt8 + '\n' + '-' * len(txt8) + '\n')
    else:
        print('-' * len(txt8) + '\n' + txt8 + '\n' + '-' * len(txt8) + '\n')

# ---------------------- #
else:
    print('-' * len(txterror) + '\n' + txterror + '\n' + '-' * len(txterror) + '\n')
    input('Preciona *Enter* para salir...')
