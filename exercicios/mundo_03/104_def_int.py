def leiaInt(numero):
  inteiro = int(input(numero))
  while inteiro not in int:
    print('Erro! Digite um número inteiro válido!')
    if type(inteiro) == int:
      break
  return inteiro


numero = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {numero}')
