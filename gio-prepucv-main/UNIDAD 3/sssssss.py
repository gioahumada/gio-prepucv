def poblar():
    lista = []
    while True:
        cadena = input()
        if cadena == 'FIN':
            return lista
        elif cadena.isdigit():
            num = int(cadena)
            if num > 0 and num not in lista:
                lista.append(num)
                
def abundante(lista):
    x = []
    for i in lista:
        suma = divisores(i)
        if suma > i:
            lista.append(i)
    return list
            

            
def divisores(num):
    suma = 0
    for i in range(1,num//2+1):
        if num % i == 0:
            suma += i
    return suma
            
lista = poblar()
abundantes = abundante(lista)

print(lista)
print(abundantes)

