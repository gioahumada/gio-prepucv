'''def crear_lista():
    n = int(input())
    lista = []
    
    for i in range(n):
        element = int(input())
        lista.append(element)
    return lista
    
def largo(lista):
    largo = len(lista)
    return largo
    
def eliminador(n1,lista):
    eliminados = 0
    for i in lista:
        if n1 in lista:
            lista.remove(n1)
            eliminados += 1
    return eliminados
    
    
    
lista = crear_lista()    
    
print('Lista Original = {}'.format(lista))
print('Largo Lista Original = {}'.format(largo(lista)))

eliminar = int(input())

print('Elemento que se elimina : {}'.format(eliminar))


print('Se eliminaron {} ocurrencia(s) de la edad {}'.format(eliminador(eliminar,lista),eliminar))

print('Lista Final = {}'.format(lista))
print('Largo Lista Final = {}'.format(largo(lista)))






'''

def pos(texto,c,p):
    i=0
    j=1
    while i<len(texto):
        if texto[i]==c:
            if j==p:
                return i
            j+=1
        i+=1
    return -1
texto = "AB;C;IWI;EE"
p1 = pos(texto,";",2)+1
p2 = pos(texto,";",3)
print(texto[p1:p2])