# Rigoberto Canales Puebla - 21.631.703-3
# Giovanni Ahumada Tapia - 21.523.921-7

# CONSTANTES, EN MAYUSCULAS PORQUE SON CONSTANTES
'''EN PYTHON EL USO DE CONSTANTES NO ES NECESARIO, ES MAS,
EL USO DE MAYUSCULAS NO DIFERENCIA EN NADA, PERO, POR UN
ORDEN VISUAL Y POR COMO FUNCIONA EN OTROS LENGUAJES, DECIDIMOS
COLOCARLAS :P '''

SHIPPING_STGO = 3000
SHIPPING_NORTE = 6000
SHIPPING_SUR = 8000

# VARIABLES A FUTURO
total_ticket = 0
stgo_total = 0 
norte_total = 0 
sur_total = 0 
debit = 0 # 
credit = 0 # 
total_debit = 0
total_credit = 0

# ENTRADA DE LA CANTIDAD DE CLIENTES
customers = int(input())

# CALCULO POR CLIENTE

for i in range(1,customers+1):
    # LEER DATOS DE CLIENTE
    rut = str(input())
    total_buy = int(input())
    m_payment = int(input())
    shipping_zone = int(input())

    # IMPRIMIR DATOS QUE NO NECESITAN CALCULOS 

    print('Rut Cliente : {}\nMonto Compra : {}'.format(rut, total_buy))

    # COMPROBAR SI EL CLIENTE PAGA CON TARJETA DE DEBITO

    if m_payment == 1:
        print('Forma de Pago : TARJETA DÉBITO')
        # SE AGREGA UN USO DE TARJETA DE DEBITO
        debit += 1
        if total_buy <= 50000:
            discount = 0
        elif total_buy > 50000 and total_buy <= 100000:
            discount = 10
        elif total_buy > 100000 and total_buy <= 500000:
            discount = 20
        else:
            discount = 40


        if discount > 0:
            discount_total = round(total_buy-((total_buy*discount)/100),0)
        else:
            discount_total = total_buy
            # SE AGREGA EL TOTAL DEL GASTO CON TARJETA DE DEBITO AL CONTADOR
        total_debit += discount_total
        
    # COMPROBAR SI EL CLIENTE PAGA CON TARJETA DE CREDITO

    else:
        print('Forma de Pago : TARJETA CRÉDITO')
        # SE AGREGA UN USO DE TARJETA DE CREDITO
        credit += 1
        if total_buy <= 50000:
            discount = 0
        elif total_buy > 50000 and total_buy <= 100000:
            discount = 5
        elif total_buy > 100000 and total_buy <= 500000:
            discount = 10
        else:
            discount = 25
        if discount > 0:
            discount_total = round(total_buy-((total_buy*discount)/100),0)
        else:
            discount_total = total_buy
            # SE AGREGA EL TOTAL DEL GASTO CON TARJETA DE CREDITO AL CONTADOR
        total_credit += discount_total
    
# - - - - - - 

    # SE AGREGA EL VALOR TOTAL, SIN IMPORTAR SI FUE HECHO CON TARJETA DE CREDITO O DEBITO
    # CABE RECALCAR QUE ESTO ESTA FUERA DE LOS IF'S DE ARRIBA 
    total_ticket += discount_total

# - - - - - - 

# VERIFICAR ZONA DE ENVIO // 1 - STGO, 2 - NORTE, 3 - SUR

    if shipping_zone == 1:
        print('Zona Destino : SANTIAGO')
        # SE AGREGA UNA PERSONA AL CONTADOR
        stgo_total += 1
        if discount_total > 100000:
            shipping_price = 0
        else:
        # SE UTILIZA LA CONSTANTE DE LA TARIFA DE ENVIO DE SANTIAGO    
            shipping_price = SHIPPING_STGO
    
    elif shipping_zone == 2:
        print('Zona Destino : NORTE')
        # SE AGREGA UNA PERSONA AL CONTADOR
        norte_total += 1
        if discount_total > 200000:
            shipping_price = 0
        else:
        # SE UTILIZA LA CONSTANTE DE LA TARIFA DE ENVIO DE ZONA NORTE
            shipping_price = SHIPPING_NORTE

    else:
        print('Zona Destino : SUR')
        # SE AGREGA UNA PERSONA AL CONTADOR
        sur_total += 1
        if discount_total > 300000:
            shipping_price = 0
        else:
        # SE UTILIZA LA CONSTANTE DE LA TARIFA DE ENVIO DE ZONA SUR
            shipping_price = SHIPPING_SUR

# SALIDA #

 # COMPROBACION DE SI EXISTIO DESCUENTO
    if discount == 0:
        print('No Tiene Descuento.')
        print('Monto total de la compra = {}\nCosto Envío = {}\nMonto final a pagar por compra y envío = ${}\n'.format(discount_total,shipping_price,discount_total+shipping_price))
    elif discount > 0:
        print('Porcentaje de descuento a aplicar = {}%'.format(discount))
        print('Monto total de la compra con descuento = {}\nCosto Envío = {}\nMonto final a pagar por compra y envío = ${}\n'.format(discount_total,shipping_price,discount_total+shipping_price))
        
# PROCESO CUANDO EL 'for' YA TERMINO

print('\nREPORTE FINAL\n')
# LA VARIABLE INTEGRA EL TOTAL CON EL DESCUENTO YA REALIZADO DE TODAS LAS TRANSACCIONES
print('Monto total recaudado por concepto de ventas = ${}'.format(total_ticket))

# PORCENTAJE DE VENTAS 
print('Porcentaje de ventas enviadas a Santiago = {}%\nPorcentaje de ventas enviadas a Zona Norte = {}% \nPorcentaje de ventas enviadas a Zona Sur = {}%'.format(round((stgo_total/customers)*100,1),round((norte_total/customers)*100,1),round((sur_total/customers)*100,1))) 
# USO DE LOS CONTADORES DE USO DE TARJETA DE DEBITO Y CREDITO
print('Total de clientes que pagaron con tarjeta de débito = {} \nTotal de clientes que pagaron con tarjeta de crédito = {}'.format(debit,credit))

# - - - - - - 

# COMPROBAR SI SE UTILIZARON TARJETAS DE DEBITO
if debit > 0:
    print('Promedio de ventas con tarjeta de débito = {}'.format(total_debit//debit))
else:
    print('No se procesaron compras con tarjeta de débito')

# COMPROBAR SI SE UTILIZARON TARJETAS DE CREDITO
if credit > 0:
    print('Promedio de ventas con tarjeta de crédito = {}'.format(total_credit//credit))
else: 
    print('No se procesaron compras con tarjeta de crédito')