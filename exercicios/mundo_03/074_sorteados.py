from random import randint
sorteados = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))

maiorMenor = sorted(sorteados)
print(f'Os valores sorteados foram: ', end='')
for sorteado in sorteados:
    print(sorteado, end=' ')

print(f'\nO maior valor sorteado foi: {maiorMenor[-1]}')
print(f'O menor valor sorteado foi: {maiorMenor[0]}')
