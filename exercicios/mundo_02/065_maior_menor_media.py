c = 'S'
cont = 0
media = 0
soma = 0
maior = -1
menor = 1

while c != 'N':
    num = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N]: ')).upper().strip()

    if num > maior:
        maior = num

    if num < maior and menor < num:
        menor = num

    cont += 1
    soma += num
    media = soma / cont

print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi: {menor}')
