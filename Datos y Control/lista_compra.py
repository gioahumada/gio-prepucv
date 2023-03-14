lista = []
menu = None

while menu != 'Q':
    menu = input('¿Que desea comprar? | Para Salir [Q]')
    if menu == 'Q':
        break
    elif menu in lista:
        print('Ya esta en la lista.')
    else:
        conf = input('Desea agregar {} a la lista? | [S] para confirmar.'.format(menu))
        if conf == 'S':
                print('Se a agregado a la lista')
                lista.append(menu)

print('La lista de compras es:')
print(lista)