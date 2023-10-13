valores = []
continuar = 'S'
cont = 0

while True:
    if continuar in 'N':
        break
    valores.append(int(input('Digite um valor: ')))
    valores.sort(reverse=True)
    cont += 1
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print(f'Você digitou {cont} elementos!')
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 NÃO faz parte da lista!')
