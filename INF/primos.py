# GIOVANNI NICOLÁS AHUMADA TAPIA - 21.523.921-7

import math as m

# - - - - - - - - - - - - - - 

def alpha(n): # N-ésimo término de la siguiente sucesión aritmética
    base = 1
    for i in range(1, n):
        base += i
    return base

def beta(x): # Es el valor obtenido al evaluar y sumar los 50 primeros términos de la siguiente serie numérica
    suma = 0
    for i in range(1,51):
        suma += (x**i)/m.factorial(i) # FACTORIAL FROM MATH -> Factorial -> Math se importo como m 
    return suma

def gama(n): # SUMATORIA de TODOS los DIVISORES positivos
    divisores = 0
    for i in range(1,n+1):
        if n % i == 0:
            divisores += i
    return divisores 

def delta(n): # SUMATORIA de TODOS los números naturales IMPARES
    n_impares = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            n_impares += i
    return n_impares

# - - - - - - - - - - - - - - - - - - - - - - - - -

# -    A N A L I S I S  D E L  P R O B L E M A    - #   

# - - - - - - - - - - - - - - - - - - - - - - - - -
     
''' Primeramente se leera el total de habitantes que desean probar la pócima. Se debe
validar que el total de habitantes sea mayor a 0 y menor o igual a 10000

Validado esto, se procedera a recpilar los datos de cada persona, los cuales son:
- Edad
- Peso
- Estatura

A estos datos se les hara un trabajo de conversion de informacion, por ejemplo:
- La edad se pasara a Meses
- El peso se pasara de kg a gr
- La estatura se pasara a metros

Todo esto para printear la informacion correspondiente de cada habitante.

Para la dosis de FELIX FELICIS que debera consumir cada habitante se utilizo la tabla brindada en el problema
para calcular la dosis, para ello se utilizo un if-elif-else calculando la edad correspondiente.

V V V V V V V V 

+--------------------+-----------------------------------------------------------------------------------------+
|   Edad en años	 |                    Fórmula para el cálculo de la dosis en mililitros                    |
+--------------------+-----------------------------------------------------------------------------------------|
|Entre 1 y 20 años 	 | (ALFA(edad en meses) * [peso en kilogramos])  / BETA(estatura en metros)                |                  
|Entre 21 y 40 años	 | ( GAMA(peso en kilogramos) * DELTA(edad en años) ) / [estatura en metros]               |
|Entre 41 y 60 años	 | (GAMA(edad en meses) * [Raíz Truncada peso en gramos]) / (estatura en cms)              |
|Mayor a 60 años	 | (DELTA(peso en kilogramos) * [Raíz Truncada de la edad en años]) / (estatura en metros) |
+--------------------+-----------------------------------------------------------------------------------------+

/\ /\ /\ /\ /\ /\ 

Las formulas utilizan funciones que no se encuentran en python, es por ello que se otorgaba la explicacion
de cada funcion para a postereor crearla.

A continuacion se explicara cada funcion, las cuales se encuentran creadas desde la linea (7) a la linea (31)

 - ALPHA :
N-ésimo término de la siguiente sucesión aritmética
[1, 2, 4, 7, 11] = 1+1 = 2 , 2+2 = 4 , 4+3 = 7 , 7+4 = 11.

Se le suma al resultado el numero corresponiente a la sucecion de numeros naturales

 - BETA : 
Es el valor obtenido al evaluar y sumar los 50 primeros términos de la siguiente serie numérica
 * Se utilizo la bibloteca de math importandola como m, con el fin de utilizar la funcion Factorial

 - GAMMA : 
SUMATORIA de TODOS los DIVISORES positivos
 * n % i == 0 se suma

 - DELTA : 
SUMATORIA de TODOS los números naturales IMPARES
 * n % 2 != 0 se suma

Hechas las funciones, se aplicaron las formulas dadas en la tabla y se TRUNCO el resultado de estas,
para posterior printearlas.

Para calcular los dias de suerte, se explicaba en el problema que 100ml de felix felicis daba 12 horas de suerte.
es por ello que, 200ml completaban un 24 horas de suerte, es decir un dia, por ello se hizo una division a los ml de
felix felicis a 200, consiguiendo asi los dias de suerte, para posterior printearlas. 
'''

while True: # VALIDAR mayor a 0 y menor o igual a 10000
    n = int(input())
    if n > 0 and n <= 10000:
        break
    
# - - - 

print('Harry, se procesarán {} habitantes del mundo mágico.\n'.format(n)) # IMPRIMIR CANTIDAD DE PERSONAS
print('----- INICIO DEL PROCESO -----\n')

for i in range(n):
    # DATOS DE ENTRADA
    edad = int(input())
    peso = int(input())
    estatura = int(input())

    meses = edad * 12 # SACAR LOS MESES DE DE VIDA DE LA PERSONA
    peso_gramos = peso * 1000 # PASAR DE KG A GRAMOS
    estatura_metros = estatura / 100 # PASAR ESTATURA A METROS

    # DATOS DE SALIDA
    print('Habitante #{}'.format(i+1))
    print('Edad : {} año(s) - {} meses.-'.format(edad,meses))
    print('Peso : {} Kg - {} g.-'.format(peso,peso_gramos))
    print('Estatura : {} cm - {} m.-'.format(estatura,estatura_metros))
    # SE UTILIZAN LOS DATOS DADOS Y SE USA EL .FORMAT PARA MOSTRARLOS EN PANTALLA.

    if edad >= 1 and edad <= 20: # Entre 1 y 20 años 
        calc = int((alpha(meses) * peso) / beta(estatura_metros))

    elif edad >= 21 and edad <= 40: # Entre 21 y 40 años 
        calc = int((gama(peso) * delta(edad)) / estatura_metros)

    elif edad >= 41 and edad <= 60: # Entre 41 y 60 años 
        raiz = int(m.sqrt(peso_gramos)) # SQRT FROM MATH -> Raiz cuadrada -> Math se importo como m 
        # SE SEPARO LA OPERACION DEBIDO A UN PROBLEMA DE MEMORIA EN PYTHON, PREFERÍ ASEGURAR MEJOR LA OPERACIÓN.
        calc = int((gama(meses)*raiz) / estatura)

    else:
        raiz = int(m.sqrt(edad)) # SQRT FROM MATH -> Raiz cuadrada -> Math se importo como m 
        # SE SEPARO LA OPERACION DEBIDO A UN PROBLEMA DE MEMORIA EN PYTHON, PREFERÍ ASEGURAR MEJOR LA OPERACIÓN.
        calc = int((delta(peso) * raiz) / estatura_metros)

    print('Dosis de FELIX FELICIS según su edad = {} ml.'.format(calc)) # SE PRINTEA CALCULO SEGUN EDAD.

    felicidad = calc // 200 
    # 100ml = 12 hrs
    # 200ml = 24 hrs -> 1 dia.

    print('El habitante tendrá {} días de SUERTE !'.format(felicidad))


    print('--------------------------------------------------')
