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
  precoFinal = preco - preco * 10 / 100
  print('Você recebeu 10% de desconto pelo pagamento em {}! Então o seu produto de R$ {:.2f} ficará por R${:.2f}'.format(pagamento, preco, precoFinal))
elif pagamento == 2:
  precoFinal = preco - preco * 5 / 100
  print('Você recebeu 5% de desconto pelo pagamento no {}! Então o seu produto de R$ {:.2f} ficará por R$ {:.2f}'.format(pagamento, preco, precoFinal))
elif pagamento == 3:
  print('Você não recebeu desconto pelo parcelamento {} no cartão! Então o seu produto de R$ {:.2f} ficará por R$ {:.2f}'.format(pagamento, preco, preco))
else:
  precoFinal = preco + preco * 20 / 100
  parcela = precoFinal / parcelas
  print(f'Sua compra será parcelada em {parcelas}x de R$ {parcela:.2f} COM JUROS')
  print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}'.format(preco, precoFinal))
