from random import choice
pc = choice(['pedra', 'papel', 'tesoura'])
user = str(input('Escolha pedra, papel ou tesoura: ')).lower().strip()
empate = (pc == 'pedra' and user == 'pedra') or (pc == 'papel' and user == 'papel') or (pc == 'tesoura' and user == 'tesoura')
lost = (pc == 'pedra' and user == 'tesoura') or (pc == 'tesoura' and user == 'papel') or (pc == 'papel' and user == 'pedra')

if empate:
  print('Você escolheu {} e a CPU escolheu {}. Então houve um empate!'.format(user, pc))
elif lost:
  print('Você escolheu {} e a CPU escolheu {}. Então {} ganha de {}. VOCÊ PERDEU!'.format(user, pc, pc, user))
else:
  print('PARABÉNS! VOCÊ VENCEU! Você escolheu {} e a CPU escolheu {}, então {} ganha de {} '.format(user, pc, user, pc))
