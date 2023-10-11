continuar = 'S'
totalDaCompra = 0.0
maisDeMil = 0
maisBarato = 0
nomeprodutoBarato = ''

while True:
    if continuar not in 'Ss':
        break
    produtoNome = str(input('Qual o nome do produto? '))
    preco = float(input('Preço R$: '))
    totalDaCompra += preco
    continuar = str(input('Quer continuar? [S/N]: '))

    if (preco > 1000):
        maisDeMil += 1

    if maisBarato == 0:
        maisBarato = preco
        nomeprodutoBarato = produtoNome
    else:
        if preco < maisBarato:
            maisBarato = preco
            nomeprodutoBarato = produtoNome

print(f'O total da compra foi R$ {totalDaCompra:.2f}')
print(f'Temos {maisDeMil} produtos custando mais de R$ 1000.00')
print(
    f'O produto mais barato foi {nomeprodutoBarato} que custa R$ {maisBarato:.2f}')
