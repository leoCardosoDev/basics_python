matriz = []
linha = 0
coluna = 0

matrizLinha1 = []
matrizLinha2 = []
matrizLinha3 = []

for i in range(0, 9):
    if coluna > 2:
        linha += 1
        coluna = 0
    valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

    if i <= 2:
        matrizLinha1.append(valor)
        coluna += 1
    elif i >= 3 and i <= 5:
        coluna += 1
        matrizLinha2.append(valor)
    elif i >= 6:
        coluna += 1
        matrizLinha3.append(valor)

matriz.insert(0, matrizLinha1)
matriz.insert(1, matrizLinha2)
matriz.insert(3, matrizLinha3)

pares = 0
soma3Coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
maioValorColuna2 = max(matriz[1])
print()
print(f'_-'*35)

for linha in matriz:
    print()
    for item in linha:
        if item % 2 == 0:
            pares += item
        print(f'[   {item}   ]', end='')
    print()
print()
print(f'_-'*35)
print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma3Coluna}')
print(f'O maior valor da segunda linha é {maioValorColuna2}')
