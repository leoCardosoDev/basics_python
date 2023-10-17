try:
  a = int(input('Numerador: '))
  b = int(input('Denominador: '))
  r = a / b
except (ValueError, TypeError):
  print(f'Tivemos um problema com os dados digitados! Eles estão incorretos!')
except ZeroDivisionError:
  print('Não é possível dividir por zero')
except KeyboardInterrupt:
  print('O usuário preferiu não informar os dados!')
else:
  print(f'O resultado é {r}')
finally:
  print('Volte sempre! Muito obrigado!')
