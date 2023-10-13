continuar = 'S'
valores = []

while True:
  if continuar in 'N':
    break
  num = int(input('Digite um valor: '))
  if num in valores:
    print('Valor duplicado! Não vou adicionar!')
  else:
    valores.append(num)
    print('Valor adicionado com sucesso!')
  continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]

valores.sort()
print(f'Você digitou os valores: {valores}')
