# ENTRADA
patente = str(input())
categoria = int(input())
tarifa = str(input())
km = float(input())

# Variables a futuro (?) # 
# ESTO PODRIA NO AGREGARSE, PERO SE MANTIENE POR UN ORDEN EN VARIABLES
peaje = None
peaje_final = None

# INFORMACION VEHICULAR, cada \n es un 'ENTER', mantenemos esto para el orden del proceso posterior
print('Vehículo Placa Patente : {}\nCategoría del Vehículo : {}\nCategoría Tarifa : {}\nDistancia recorrida por el vehículo = {} kms.'.format(patente,categoria,tarifa,km))

'''DATA
DE LOS VEHICULOS

SE OBTIENE PRIMERAMENTE LA CATEGORIA DEL VEHICULO
LUEGO SE REVISA LA TARIFA PARA CALCULAR EL VALOR DEL PEAJE
SEGUN LA TABLA DE PRECIOS '''

# CATEGORIA 1 - Motos, motonetas, autos y camionetas #
if categoria == 1:
    if tarifa == 'BAJA':
        peaje = int(90*km)
    elif tarifa == 'MEDIA':
        peaje = int(180*km)
    else:
        peaje = int(270*km)

# CATEGORIA 2 - Buses y camiones #
elif categoria == 2:
    if tarifa == 'BAJA':
        peaje = int(180*km)
    elif tarifa == 'MEDIA':
        peaje = int(360*km)
    else:
        peaje = int(540*km)
        
# CATEGORIA 3 - Buses y camiones con remolque #    
elif categoria == 3:
    if tarifa == 'BAJA':
        peaje = int(260*km)
    elif tarifa == 'MEDIA':
        peaje = int(520*km)
    else:
        peaje = int(780*km)
    
# CATEGORIA 4 - Autos y camionetas con remolque #    
else:
    if tarifa == 'BAJA':
        peaje = int(100*km)
    elif tarifa == 'MEDIA':
        peaje = int(300*km)
    else:
        peaje = int(500*km)

 #  VV  VV    VALOR DEL PEAJE SIN DESCUENTO     VV  VV

print('Valor del peaje calculado es ${}'.format(peaje))

'''SE VERIFICA SI ES NECESARIO
 APLICAR UN DESCUENTO '''

if peaje < 2000:
    print('No se aplica descuento')
elif peaje >= 2000 and peaje < 5000:
    peaje_final = int(peaje * 93/100)
    print('Se aplica descuento del 7%\nValor Final del peaje a pagar es ${}'.format(peaje_final))
elif peaje >= 5000 and peaje <= 10000:
    peaje_final = int(peaje * 88/100)
    print('Se aplica descuento del 12%\nValor Final del peaje a pagar es ${}'.format(peaje_final))
else:
    peaje_final = int(peaje * 85/100)
    print('Se aplica descuento del 15%\nValor Final del peaje a pagar es ${}'.format(peaje_final))