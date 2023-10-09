preco = float(input('Qual o valor do produto? R$ '))
pagamento = str(input('Qual vai ser a forma de pagamento? '))

if pagamento == 'dinheiro':
  precoFinal = preco - preco * 10 / 100
  print('Você recebeu 10% de desconto pelo pagamento em {}! Então o seu produto de R$ {:.2f} ficará por R${:.2f}'.format(pagamento, preco, precoFinal))
elif pagamento == 'cartão':
  precoFinal = preco - preco * 5 / 100
  print('Você recebeu 5% de desconto pelo pagamento no {}! Então o seu produto de R$ {:.2f} ficará por R$ {:.2f}'.format(pagamento, preco, precoFinal))
elif pagamento == '2x':
  print('Você não recebeu desconto pelo parcelamento {} no cartão! Então o seu produto de R$ {:.2f} ficará por R$ {:.2f}'.format(pagamento, preco, preco))
else:
  precoFinal = preco + preco * 20 / 100
  print('Você vai pagar 20% de juros pelo parcelamento {}! Então o seu produto de R$ {:.2f} ficará por R$ {:.2f}'.format(pagamento, preco, precoFinal))
