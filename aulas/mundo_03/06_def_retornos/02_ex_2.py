def contador(inicio, fim, passo):
  contador = inicio
  while contador <= fim:
    print(f'{contador} ', end='')
    contador += passo
  print()

contador(2, 10, 2)
