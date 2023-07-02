import os
os.system ("clear") 

print()

def invertir_digitos(n):
    espejo = 0
    while n > 0:
        digito = n % 10
        espejo = espejo * 10 + digito
        n //= 10
    return espejo

print('invertir_digitos(142)')
print(invertir_digitos(142))

print()

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print('es_primo(17)')
print(es_primo(17))

print()

def agregar_primos(n):
    lista = []
    for i in range(n+1):
        if es_primo(i) == True:
            lista.append(i)

    return lista

print('agregar_primos(19)')
print(agregar_primos(19))

print()

def promedio(lista):
    largo = len(lista)
    suma = sum(lista)
    suma /= largo
    return suma

lista = [7.0, 3.1, 1.7]
print('Notas : {}'.format(lista))
print('Promedio: {}'.format(promedio(lista)))


def f(a, b):
    c = a + 2 * b
    d = b ** 2
    return c + d

a = 3
b = 2
c = f(b, a)
d = f(a, b)
print(c, d)

def f(x):
    a = x ** 2
    b = a + g(a)
    return a * b

def g(x):
    a = x * 3
    return a ** 2

m = f(1)
n = g(1)
print(m, n)

def f(n):
    if n == 0 or n == 1:
        return 1
    a = f(n - 2)
    b = f(n - 1)
    s = a + b
    return s

print(f(5))
