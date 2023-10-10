frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'{junto} -> -> {inverso}')
print(f'As frase {junto} ', end='')
if junto != inverso:
    print(f'NÃO É UM ', end='')
else:
    print('É UM ', end='')
print('PALÍNDROMO')
