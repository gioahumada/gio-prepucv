def LeerValidar (limInf , limSup) :
    numero = int(input("Ingrese un número : "))
    while (numero < limInf) or (numero > limSup) : 
        print("Número debe estar entre [", limInf,
        numero = int(input("Ingrese un número : "))
    return numero
", limSup,
# Programa Principal & llamada a la función
numeroLeido = LeerValidar(1,100)
print("Número leído y Validado =", numeroleido)