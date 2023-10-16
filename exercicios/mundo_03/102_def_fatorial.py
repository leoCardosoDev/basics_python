def fatorial(numero, show=False):
  contador = numero
  resultado = 1
  while contador > 0:
    if show: 
      print(f'{contador}', end='')
      print(f' x ' if contador > 1 else ' = ', end='')
    resultado *= contador
    contador -= 1
  return resultado


numero = int(input('Digite um número: '))
print(fatorial(numero, True))
