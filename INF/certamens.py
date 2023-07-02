import math as m

def es_primo(n):
    if n <= 1:
        return False
    
    for i in range(2,int(m.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def primo_der(n):
    while n > 0:
        if es_primo(n) == True:
            n //= 10
        else:
            return False
    return True

def sumatoria(n):
    raiz = int(m.sqrt(n))
    suma = 0

    for i in range(1,raiz+1):
        suma += 1/i
    return int(suma) * n

def longitud(n):
    n = sumatoria(n)
    long = 0
    while n > 0:
        n //= 10
        long += 1

    return long

def es_par(n):
    if longitud(n) % 2 == 0:
        return False
    else:
        return True



    

x = 7393
print(x,primo_der(x))

x = 521
print(x,es_par(x))

