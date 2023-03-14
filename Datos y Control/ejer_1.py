texto = input('Revisor de Texto (Espacios, puntos, comas.) \n Coloca tu texto aqui: \n')
esp = 0
pun = 0
com = 0

for espacios in texto:
    if espacios in ' ':
        esp += 1

for puntos in texto:
    if puntos in '.':
        pun += 1

for comas in texto:
    if comas in ',':
        com += 1

print('\nSe a encontrado {} Espacios, {} Puntos y {} Comas en tu texto.'.format(esp, pun, com))
