import math

def n_espejo(n):
    espejo = 0
    while n > 0:
        digito = n % 10
        espejo = espejo * 10 + digito
        n //= 10

    return espejo

x = 74575
print(x,n_espejo(x))

print(math.pi)