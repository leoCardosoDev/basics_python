listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Tranferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)

print('-'*60)
print(f'{"Listagem de preços - Primeira Forma":^60}')
print('-'*60)
for i in range(0, len(listagem), 2):
    nome = listagem[i]
    preco = listagem[i+1]
    print(f'{nome:.<30}R$ {preco:>7.2f}')

print('-'*50)
print(f'{"Listagem de preços - Segunda Forma":^50}')
print('-'*50)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
        print(f'R$ {listagem[pos+1]:>8.2f}')
