from random import randint
valores = []
for i in range(0, 5):
    valores.append(randint(1, 9))

for v in valores:
    print(f'{v}...', end='')

for i in range(0, 5):
    valores.append(int(input('\nDigite um valor: ')))

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}...')


