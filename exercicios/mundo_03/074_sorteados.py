from random import randint
a = (randint(1, 9),)
b = (randint(1, 9),)
c = (randint(1, 9),)
d = (randint(1, 9),)
e = (randint(1, 9),)

sorteados = (a+b+c+d+e)
maiorMenor = sorted(sorteados)
print(f'Os valores sorteados foram: ', end='')
for sorteado in sorteados:
    print(sorteado, end=' ')

print(f'\nO maior valor sorteado foi: {maiorMenor[-1]}')
print(f'O menor valor sorteado foi: {maiorMenor[0]}')
