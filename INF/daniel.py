n = int(input())
while n < 4 or n >= 101:
    n = int(input())
    
for i in range(n):
    rut = str(input())
    teorica = int(input())
    practica = int(input())
    ingles = int(input())
    
    teorica_promedio = (teorica*100)/0.3
    practica_promedio = (practica*100)/0.5
    ingles_promedio = (teorica*100)/0.2
    
    promedio = teorica_promedio + practica_promedio + ingles_promedio
    print(rut)