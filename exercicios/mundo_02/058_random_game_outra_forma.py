from random import randint
computador = randint(0, 10)
print('Olá, sou seu computador... Acabei de pensar num número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('É maior... Tente outra vez: ')
        else:
            print('É menor... Tente outra vez')
print(f'Acertou com {palpites} tentativas! Parabéns!')
