a = ['a', 'e', 'i', 'o', 'u']
frase = 'Hola gente como esta'
vocales = 0

for letras in frase:
    if letras in a:
        print('He encontrado {}.'.format(letras))
        vocales += 1

print('Vocales encontradas {}'.format(vocales))
