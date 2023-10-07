frase = str(input('Digite uma frase completa: '))
print('A letra "A" aparece {} vezes'.format(frase.upper().strip().count('A')))
print(frase.find('a'))
print(frase.rfind('a'))
