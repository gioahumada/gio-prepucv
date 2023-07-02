# Giovanni Nicolás Ahumada Tapia - 21.523.921-7

import math as m

# - - - - FUNCIONES - - - - #

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(m.sqrt(n)+1)): # Proceso para ahorrar memoria
        if n % i == 0:
            return False
    return True
# Devuelve TRUE OR FALSE

def patito(n):
    while n != 0:
        digito = n % 10
        if digito == 2:
            return True
        n //= 10
    return False
# Devuelve TRUE OR FALSE

def alpha(n): # Suma de todos los digitos impares
    sum_impares = 0
    while n != 0:
        digito = n % 10
        if digito % 2 != 0:
            sum_impares += digito
        n //= 10
    return sum_impares
# Devuelve un Numero

def beta(n): # Cantidad de N° pares
    pares = 0
    while n != 0:
        digito = n % 10
        if digito % 2 == 0:
            pares += 1
        n //= 10
    return pares
# Devuelve un Numero


def gama(n): # Raiz cuadrada de la sumatoria de N° Naturales
    suma = 0
    for i in range(n+1):
        suma += i
    raiz = int(m.sqrt(suma))
    return raiz
# Devuelve un Numero

def delta(n): # N-esimo termino de la sucecion 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37...
    if n == 0 or n == 1 or n == 2:
        return 1
    
    n1 = 1
    n2 = 1
    n3 = 1
    
    for i in range(3, n + 1): #Si el rango iniciara en 2 no tendria sentido por la intruccion anterior
        s = n1 + n2
        n1 = n2 
        n2 = n3
        n3 = s
    
    return n3
# Devuelve un Numero

# - - - - - - - - - #

'''# ANALISIS DEL PROBLEMA #'''

'''En el colegio Hogwarts los estudiante deben cumplir con los examenes
 Título Indispensable de Magia Ordinaria.
 
 Este examen coloca en panico a muchos estudiantes, es por ello que, Harry Potter
 ha decidido preparar un caldero de filtro de paz, para crear una pocima
 que calma la ansiedad, la cual, debe ser consumida en dosis calculadas cuidadosamente,
 de modo contrario, podria generar un sueño profundo irreversible.
 
 Para calcular la dosis se reciben 4 datos:
 - Rut
 - Dia
 - Mes
 - Año

 Segun el mes de nacimiento se realiza un calculo para recibir la dosis en centimetros cubicos:

|    # Primer semestre de un año (Primeros 6 meses)
|     - SI 5 últimos dígitos del rut forman un número primo :
|       dosis = alfa(rut)  * gama(día de nacimiento)  / delta(mes de nacimiento)   
|   
|     - SI 5 últimos dígitos del rut NO forman un número primo :
|       dosis = beta(rut) * gama(año de nacimiento) / delta(día de nacimiento) 

* Un numero es primo si es divisible por si mismo, se calculan los 5 ult digitos con un modulo 100000

|    # Segundo semestre de un año (Ultimos 6 meses)	
|     - SI rut es un número patito :
|     dosis =  beta(rut) * gama(año de nacimiento) / delta(beta(año de nacimiento))
|
|     - SI rut NO es un número patito :
|     dosis =  alfa(rut) * gama(mes de nacimiento)  / delta(alfa(día de nacimiento))
 
* Un numero patito es algun numero que tenga al menos un digito igual a 2

----

Si la dosis calculada es mayor a 70cc (10cc -> 1 dia), significara que el estudiante tendra suficiente dosis
y estara relajado para una semana de examenes

De no ser asi, el estudiante NO estara relajado.


 '''

# - - - - - - - - - #

print('----- INICIO DEL PROCESO -----\n')

n_estudiante = 1 # Contador estudiante fuera del bucle


while True:
    segundo_semestre = False # Aun no se define si pertenece al primero o segundo

    rut = int(input()) 
    if rut == 0: # Si el rut es 0, se termina el bucle
        break

# DATOS DE ENTRADA

    dia = int(input())
    mes = int(input())
    ano = int(input()) # No se si en python se puede usar variables con caracteres en español

# DATOS DE SALIDA

    print('Estudiante # {}'.format(n_estudiante)) # Uso del contador de estudiantes

    n_estudiante += 1 # Suma al contador de estudiantes

    print('Rut : {}'.format(rut))
    print('Fecha de Nacimiento : {} - {} - {}'.format(dia,mes,ano))

    if mes > 6: # Verificar si pertenece al segundo semestre
        segundo_semestre = True 

    rut_5_primo = es_primo(rut % 100000) # Se usa modulo 100.000 para sacar los ult. 5 digitos
    # Retorna True or False
    
    rut_patito = patito(rut) # Patito = Algun digito igual a 2
    # Retorna True or False

    if segundo_semestre == False and rut_5_primo == True: # Primer Semestre, 5 ult digitos Primos
        print('Primer Semestre & primo 5 últimos dígitos del rut')
        dosis = round(alpha(rut) * gama(dia) / delta(mes))
        print('Dosis = {} cc'.format(dosis))
        
    elif segundo_semestre == False and rut_5_primo == False: # Solo Primer Semestre
        print('Primer Semestre & NO primo 5 últimos dígitos del rut')
        dosis = round(beta(rut) * gama(ano) / delta(dia))
        print('Dosis = {} cc'.format(dosis))

    elif segundo_semestre == True and rut_patito == True: # Segundo semestre, Rut patito
        print('Segundo Semestre & rut patito')
        dosis = round(beta(rut) * gama(ano) / delta(beta(ano)))
        print('Dosis = {} cc'.format(dosis))
    
    else:                                                 # Solo segundo semestre
        print('Segundo Semestre & rut NO patito')
        dosis = round(alpha(rut) * gama(mes) / delta(alpha(dia)))
        print('Dosis = {} cc'.format(dosis))

    if dosis >= 70: 
        # 10cc -> 24 hrs -> 1 dia
        # 70cc -> 7 dias

        print('Estudiante tiene suficiente dosis y estará relajado durante toda la semana de examen !!')
    else:
        print('Estudiante NO tiene suficiente dosis y NO estará relajado durante la semana de examen')

    print('')


print('----- FIN DEL PROCESO -----')