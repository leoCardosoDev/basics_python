# for c in range(0, 6):
#     n = int(input('Digite um numero: '))
#     if n % 2 == 0:
#         par = n
#         print(f'{n} + {par} = {par + n }')
# print('FIM')

soma = 0
cont = 0
for c in range(0,6):
  n = int(input('Digite um número: '))
  if n % 2 == 0:
    soma += n
    cont+= 1
print(f'Você informou {cont} números pares e a soma foi {soma}')
