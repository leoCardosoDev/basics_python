from random import sample
from time import sleep

print('-'*40)
print(f'JOGA NA MEGA SENA DA VIRADA'.rjust(45))
jogos = []
numeros_disponivel= list(range(1,61))
num = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {num} Jogos')

for i in range(0, num):
  numeros_escolhidos = sample(numeros_disponivel, 6)
  sleep(1)
  print(f'Jogo {i+1}: {numeros_escolhidos}')
