from random import randint
ganhou = True
cont = 0

while True:
    if ganhou != True:
        break
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + computador
    parOuImpar = ' '
    while parOuImpar not in 'PI':
        parOuImpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    ganhou = parOuImpar == 'P' and soma % 2 == 0 or parOuImpar == 'I' and soma % 2 == 1
    if ganhou:
        print('Você GANHOU!')
        cont += 1
print('Você PERDEU!')
print(f'GAME OVER! Você venceu {cont}')
