from time import sleep

def maior(*valores):
  print('Analisando os valores passados...')
  contador = 0
  if valores:
    ma = max(valores)
  else:
    ma = 0
  for valor in valores:
    contador += 1
    print(f'{valor} ', end='', flush=True)
    sleep(.5)
  print(f' Foram informados {contador} ao todo')
  print(f'O maior valor informado foi o {ma}')


maior(2, 9, 4, 5, 7, 1)
maior(4,7,0)
maior(1, 2)
maior(6)
maior()
