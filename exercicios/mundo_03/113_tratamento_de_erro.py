def leiaInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print('\033[1;31mERRO: por favor, digite um número válido!\033[m')
      continue
    except KeyboardInterrupt:
      print('\n\033[1;31mEntrada de dados interrompida pelo usuário!\033[m')
      return 0
    else:
      return n
    
    
def leiaFloat(msg):
  while True:
    try:
      n = float(input(msg))
    except (ValueError, TypeError):
      print('\n\033[1;31mErro! Por favor, digite um número real válido\033[m')
      continue
    except KeyboardInterrupt:
      print(f'\n\033[1;31mErro! Usuário preferiu interromper o programa!')
      return 0
    else:
      return n
  

n1= leiaInt('Digite um valor inteiro: ')
n2 = leiaInt('Digite um valor real: ')
print(n1)
print(n2)
