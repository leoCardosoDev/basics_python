preco = float(input('Qual o valor do produto? R$ '))
pagamento = int(input('''Qual vai ser a forma de pagamento?:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
'''))
if pagamento == 4: 
  parcelas = int(input('Quantas parcelas? '))

if pagamento == 1:
  total = preco - preco * 10 / 100
elif pagamento == 2:
  total = preco - preco * 5 / 100
elif pagamento == 4:
  total = preco + preco * 20 / 100
  parcela = total / parcelas
  print(f'Sua compra será parcelada em {parcelas}x de R$ {parcela:.2f} COM JUROS')
elif pagamento == 3:
  total = preco
  print(f'Sua compra será parcelada em 2x de R$ {preco / 2 :.2f} SEM JUROS')
else:
  total = 0
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}'.format(preco, total))
