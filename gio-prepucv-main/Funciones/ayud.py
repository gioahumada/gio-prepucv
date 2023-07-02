p = int(input())

si = 0
no = 0

for i in range(1,p+1):
    nota = float(input())
    if nota >= 4:
        si += 1
    elif nota < 4:
        no += 1

print('porcentaje de aprobados = {} %\nporcentaje de reprobados = {} %'.format((si*100)/p,(no*100)/p))