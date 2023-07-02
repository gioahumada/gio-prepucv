n = int(input())

reprobados = 0 
aprobados = 0
promedio_puntajes = 0

bajo = 0
medio = 0 
alto = 0
while True:
    if n >= 4 and n < 101:
        break
    else:
        n = int(input())
print('Total de Profesionales que Rindieron EXAMEN 2021 = {}\n'.format(n))
for i in range(n):

    rut = input()
    teorica = int(input())
    practica = int(input())
    ingles = int(input())
    
    promedio_teorica = (teorica*0.3)
    promedio_practica = (practica*0.5)
    promedio_ingles = (ingles*0.2)
    
    promedio = int(promedio_teorica+promedio_practica+promedio_ingles)

    
    print('Profesional rut {}'.format(rut))
    
    if promedio < 60:
        print('REPRUEBA EUNACOINF\n')
        reprobados =+1
    elif promedio >= 60 and promedio < 70:
        print('APRUEBA EUNACOINF\nPuntaje Final = {}\nNIVEL DE COMPETENCIA BAJO\n'.format(promedio))
        aprobados += 1
        bajo += 1
        promedio_puntajes += promedio
    elif promedio > 70 and promedio < 81:
        aprobados += 1
        medio += 1
        promedio_puntajes += promedio
        print('APRUEBA EUNACOINF\nPuntaje Final = {}\nNIVEL DE COMPETENCIA MEDIO\n'.format(promedio))
    else:
        aprobados += 1
        alto += 1
        promedio_puntajes += promedio
        print('APRUEBA EUNACOINF\nPuntaje Final = {}\nNIVEL DE COMPETENCIA ALTO\n'.format(promedio))

print('El {}% de los profesionales APROBÓ el examen.'.format(round((aprobados*100)/n,1)))
print('El {}% de los profesionales REPROBÓ el examen.'.format(round((reprobados*100)/n,1)))
if aprobados == 0:
    print('NADIE aprobó el examen.')
else:
    print('El promedio de puntajes de los aprobados fue {}'.format(round(promedio_puntajes/aprobados,1)))
    print('El {}% de los profesionales que aprobó el examen tiene un nivel de competencia BAJO.'.format(round((bajo/aprobados)*100,1)))
    print('El {}% de los profesionales que aprobó el examen tiene un nivel de competencia MEDIO.'.format(round((medio/aprobados)*100,1)))
    print('El {}% de los profesionales que aprobó el examen tiene un nivel de competencia ALTO.'.format(round((alto/aprobados)*100,1)))
        