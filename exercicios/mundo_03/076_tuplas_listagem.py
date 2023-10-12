listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25)
for i in range(0, len(listagem), 2):
    nome = listagem[i]
    preco = listagem[i+1]
    print(f'{nome:.<40}R$ {preco:>8.2f}')
