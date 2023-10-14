matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
somaColuna = 0
maiorValor = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha}, {coluna}]:'))
print('-_' * 30)
for linha in range(0, 3):
    somaColuna += matriz[linha][2]
    maiorValor = max(matriz[1])
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
    print()
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da 3ª coluna é {somaColuna}')
print(f'O maior valor da 2ª linha é {maiorValor}')
