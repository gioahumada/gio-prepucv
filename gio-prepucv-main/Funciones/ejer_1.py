n1 = 0
n2 = 0
op = None
def numeros():
    n1 = input('¿Cual es tu primer numero?')
    n2 = input('¿Cual es tu segundo numero?')


def main():
    print('Calculadora interactiva')
    op = input('Dime que operacion deseas realizar... \n A = SUMA \n B = RESTA \n C = MULTIPLICACION \n D = DIVISION \n')
    if op == 'A':
        numeros()
        s = n1 + n2
        print('El resultado es: {}'.format(s))
    elif op == 'B':
        numeros()
        b = n1 + n2
        print('El resultado es: {}'.format(b))
    elif op == 'C':
        numeros()
        b = n1 + n2
        print('El resultado es: {}'.format(b))
    elif op == 'D':
        numeros()
        b = n1 + n2
        print('El resultado es: {}'.format(b))
    else:
        exit

if __name__ == '__main__':
    main()