import math as m
import os

os.system ("clear") 

print('\n--------------------\n')

def es_primo(n):
    if n <= 1:
        return False
    
    for i in range(2,int(m.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print('# es_primo')
x = 3
print(x,es_primo(x))
x = 20
print(x,es_primo(x))

print('\n--------------------\n')

def tiene_siete(n):
    while n > 0:
        digito = n % 10
        if digito == 7:
            return True
        n //= 10
    return False

print('# tiene_siete')
x = 4723
print(x,tiene_siete(x))
x = 72941
print(x,tiene_siete(x))
x = 453213
print(x,tiene_siete(x))

print('\n--------------------\n')

def espejo(n):
    espejo = 0
    while n > 0:
        digito = n % 10
        espejo = espejo * 10 + digito
        n //= 10

    return espejo

print('# espejo')
x = 24837
print(x,espejo(x))
x = 123456
print(x,espejo(x))

print('\n--------------------\n')

def es_par(n):
    if n % 2 == 0:
        return True
    return False

print('# es par')
x = 22
print(x,es_par(x))
x = 23
print(x,es_par(x))

print('\n--------------------\n')


def pos_numero(a,b):
    a = a // 10 ** b+1
    digito = a % 10
    return digito

print(pos_numero(12345,2))
    


