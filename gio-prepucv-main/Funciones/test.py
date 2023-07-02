n1 = int(input())
n2 = int(input())

print('Números enteros en el rango de {} a {} :'.format(n1,n2))
for n in range(n1,n2+1):
    print(n, end = '-')