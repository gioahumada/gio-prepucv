while True:
    n = int(input())
    if n >= 1 and n <= 100:
        break
    
numero = 1    
for i in range(n):
    if i != n:
        print(numero, end= '.')
    else:
        print(numero, end = ',')
        numero += 3
        