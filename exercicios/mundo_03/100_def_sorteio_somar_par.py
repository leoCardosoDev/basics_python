from random import randint
from time import sleep

numeros_sorteados = []

def sorteio():
  print(f'Sorteando 5 valores da lista: ', end='', flush=True)
  for i in range(0, 5):
    numeros_sorteados.insert(i, randint(1, 9))
    print(f'{numeros_sorteados[i]} ', end='', flush=True)
    sleep(.5)
  print('PRONTO!')


def somar():
  soma = 0
  for i in numeros_sorteados:
    if i % 2 == 0:
      soma += i
  print(f'Somando os valores pares de {numeros_sorteados}, temos = {soma}')


sorteio()
somar()
