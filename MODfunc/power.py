def power(a,b):
    num = a
    for i in range(b-1):
        num *= a

    return int(num)

def main():
    a = int(input("Numero base:"))
    b = int(input("Numero Exponente:"))
    resultado = power(a,b)
    print("Resultado {}".format(resultado))

if __name__ == "__main__":
    main()