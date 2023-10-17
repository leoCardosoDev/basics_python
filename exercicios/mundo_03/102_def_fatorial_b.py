def fatorial(numero, show=False):
  resultado = 1
  for contador in range(numero, 0 , -1):
    if show: 
      print(f'{contador}', end='')
      print(f' x ' if contador > 1 else ' = ', end='')
    resultado *= contador
  return resultado


numero = int(input('Digite um número: '))
print(fatorial(numero, True))
