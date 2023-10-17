def leiaInt(numero):
  inteiro = input(numero)
  isValidInt = inteiro.isalnum() or inteiro.isalpha() or inteiro.isspace()
  while isValidInt:
    if inteiro.isnumeric():
      break
    print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
    inteiro = input(numero)  
  return inteiro


numero = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {numero}')
