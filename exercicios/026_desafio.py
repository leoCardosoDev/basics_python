frase = str(input('Digite uma frase completa: ')).lower().strip()
print('A letra "A" aparece {} vezes'.format(frase.count('a')))
print(frase.find('a'))
print(frase.rfind('a'))
