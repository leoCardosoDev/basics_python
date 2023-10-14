matriz = []
matrizLinha1 = []
matrizLinha2 = []
matrizLinha3 = []
linha = 0
coluna = 0

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
print()
print(f'_-'*35)
for linha in matriz:
    print()
    for item in linha:
        print(f'[{item:^5}]', end='')
    print()
print()
print(f'_-'*35)
print()
