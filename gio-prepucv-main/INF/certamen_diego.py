while True:
    conductores = int(input())

    if conductores > 0 or conductores <= 1000:
        break

bajoInfluenciaAlcohol = 0
totalGradosAlcoholBIA = 0

totalReincidencias = 1

totalSuspensionLarga = 0

estadoEbriedad = 0
totalGradosAlcoholEDE = 0

print(f"Hay {conductores} conductores infractores")

for i in range(1, conductores + 1):
    rut = input()
    gradoAlcohol = float(input())
    reincidencia = int(input())
    dañoCausado = int(input())

    if gradoAlcohol >= 0.3 and gradoAlcohol < 0.8:
        influenciaAlcohol = "BAJO LA INFLUENCIA DEL ALCOHOL"
        totalGradosAlcoholBIA += gradoAlcohol

        if reincidencia > 1:
            totalReincidencias += 1
        
    else:
        influenciaAlcohol = "EN ESTADO DE EBRIEDAD"
        totalGradosAlcoholEDE += gradoAlcohol

    if dañoCausado == 1:
        dañoCausado = "SIN DAÑOS NI LESIONES"
        multa = "5 UTM"
        pena = 0

        if reincidencia == 1:
            suspension = 3

        else:
            suspension = 72

    elif dañoCausado == 2:
        dañoCausado = "DAÑOS MATERIALES O LESIONES LEVES"
        multa = "5 UTM"
        pena = 0

        if reincidencia == 1:
            suspension = 6
        
        else:
            suspension = 72

    elif dañoCausado == 3:
        dañoCausado = "LESIONES MENOS GRAVES"
        multa = "10 UTM"
        pena = 20

        if reincidencia == 1:
            suspension = 9
        else:
            suspension = 72

    elif dañoCausado == 4:
        dañoCausado = "LESIONES GRAVES"
        multa = "20 UTM"
        pena = 541

        if reincidencia == 1:
            suspension = 36
        else:
            suspension = 72

    elif dañoCausado == 5:
        dañoCausado = "LESIONES GRAVISIMAS"
        multa = "30 UTM"
        pena = 365 * 5

        if reincidencia == 1:
            suspension = 60
        else:
            suspension = 72

    else:
        dañoCausado = "MUERTE"
        multa = "30 UTM"
        pena = 365 * 5

        if reincidencia == 1:
            suspension = 60

        else:
            suspension = 72

    if suspension > 36:
        totalSuspensionLarga += 1

    print(f"CONDUCTOR INFRACTOR {i} - RUT : {rut}\nESTADO ETÍLICO : {influenciaAlcohol}\nREINCIDENCIA(S) : {reincidencia}\nTIPO DE LESIÓN O DAÑO QUE CAUSÓ  : {dañoCausado}")

    if influenciaAlcohol == "BAJO LA INFLUENCIA DEL ALCOHOL":
        bajoInfluenciaAlcohol += 1
        print(f"TIEMPO MÁXIMO DE SUSPENSIÓN : {suspension} MESES\nMULTA MÁXIMA : {multa} UTM\nPENA PRIVATIVA MÁXIMA = {pena} DÍAS")

print("\nREPORTE FINAL\n\n")

if bajoInfluenciaAlcohol > 0:
    porcentajeBIA = round((bajoInfluenciaAlcohol * 100) / conductores, 2)
    promGradosAlcoholIBA = round(totalGradosAlcoholBIA / bajoInfluenciaAlcohol, 1)
    print(f"EL {porcentajeBIA}% CONDUCÍA BAJO LA INFLUENCIA DEL ALCOHOL\nPROMEDIO DE GRADOS DE ALCOHOL POR LITRO DE SANGRE = {promGradosAlcoholIBA}\nCONDUCTORES REINCIDENTES : {totalReincidencias}\n")

if estadoEbriedad > 0:
    porcentajeEDE = round((estadoEbriedad * 100) / conductores, 2)
    promGradosAlcoholEDE = round(totalGradosAlcoholEDE / estadoEbriedad, 1)
    print(f"EL {porcentajeEDE}% CONDUCÍA EN ESTADO DE EBRIEDAD\nPROMEDIO DE GRADOS DE ALCOHOL POR LITRO DE SANGRE = {promGradosAlcoholEDE}\nCONDUCTORES CON SUSPENSIÓN DE LICENCIA SUPERIOR A 3 AÑOS : {totalSuspensionLarga}")