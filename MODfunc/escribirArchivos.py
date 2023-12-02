import time

SALIDA = "SALIR"

def hora():
    ahora = time.localtime()
    cadena_fecha_hora = time.strftime("%d/%m/%Y %H:%M:%S", ahora)
    return cadena_fecha_hora

def preguntar():
    return input("Introduce un producto a tu canasto. Retorna [{}] para salir".format(SALIDA))

def main():
    lista = []

    usuario = preguntar()

    while usuario != SALIDA:
        lista.append(usuario)
        print("\n".join(lista))
        usuario = preguntar()
    
    a = open("MODfunc/compra.txt", "w")
    a.write(hora() + "\n")
    a.write("\n".join(lista))
    a.close()

if __name__ == "__main__":
    main()

