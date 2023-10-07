vkm = int(input('Qual a distância da viagem em km? '))
if vkm > 200:
    preco = vkm * 0.45
else:
    preco = vkm * 0.50
print('Você pagará R$ {:.2f} pela viagem!'.format(preco))
