numero = int(input('Numero a multiplicar: '))

for n in range(1,11):
    if n % 2 == 0:
        print('{} x {} = {}'.format(numero, n, numero * n))