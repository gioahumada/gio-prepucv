# BAJO INFLUENCIA DEL ALCOHOL SI LT POR SANGRE >= 0.3 y menor a 0.8
# ESTADO DE EBRIEDAD: si su grado de alcohol x lt de sangre es mayor o igual a 0.8

# Leer la cantidad de infractores a procesar, validar que el numero sea mayor a 0 y menor o igual a 1000
# Mostrar la cantidad de conductores infractores de la ley que se deben procesar

# Leer rut
#leer su grado de alcohol por lt de sangre, valor ingresado igual o mayor a 0.3
# Leer su reeincidencia
# Leer el tipo de lesion que causo
# Leer su reincidencia
# Tipo de daño que causo
    # 1 - Sin daños ni lesiones
    # 2 - Daños materiales o lesiones graves
    # 3 - Lesiones menos graves
    # 4 - Lesiones graves
    # 5 - Lesiones gravisimas
    # 6 - Muerte

while True:
    infractores = int(input())
    if infractores > 0 and infractores <= 1000:
        break

print('Cantidad de infractores a procesar : {}'.format(infractores))


for i in range(infractores):
    rut = str(input())
    lt_alcohol = float(input())
    reincidencia = int(input())
    daños = int(input())

    print('Infractor {}'.format(i+1))
    print(rut)


    if lt_alcohol >= 0.3 and lt_alcohol < 0.8:
        print('a')
        
    else:
        print('Estado de ebriedad')

    print('N° de Reincidencia : {}'.format(reincidencia))
    print('Tipo de lesión o daño causado : {}'.format(daños))

    if daños == 1:
        print('Sin daños ni lesiones')
    elif daños == 2:
        print('Daños materiales o lesiones graves')
    elif daños == 3:
        print('Lesiones menos graves')
    elif daños == 4:
        print('Lesiones graves')
    elif daños == 5:
        print('Lesiones gravisimas')
    else:
        print('Muerte')

    if lt_alcohol >= 0.3 and lt_alcohol < 0.8 and reincidencia == 1:
        print('')
