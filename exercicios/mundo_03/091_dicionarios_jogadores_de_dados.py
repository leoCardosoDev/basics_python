from random import randint
from time import sleep

jogadores = {}

for i in range(0, 4):
  jogadores[i] = randint(1,6)
  sleep(1)
  print(f'O jogador{i+1} tirou {jogadores[i]}')
i = 1
for chave, valor in sorted(jogadores.items(), key=lambda item: item[1], reverse=True):
  sleep(1.5)
  print(f'{i}º lugar: jogador{chave+1} com {valor}')
  i+=1
