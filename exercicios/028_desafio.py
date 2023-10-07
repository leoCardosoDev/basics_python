from random import randint
pc = randint(1, 5)
user = int(input('Adivinhe o número de 1 a 5: '))
if user == pc:
    print('Número foi: {}! Você ganhou ao escolher: {}!'.format(pc, user))
else:
    print('Número foi: {}! Você perdeu ao escolher: {}!'.format(pc, user))
