num = []
for i in range(0, 5):
    num.insert(i, int(input(f'Digite um valor para a posição {i}: ')))
print(f'Você digitou os valores: {num}')
print(f'\nO maior valor digitado foi {max(num)} na(s) posição(ões): ', end='')
for ma, n in enumerate(num):
    if max(num) == n:
      print(f'{ma}... ', end='')
print(f'\nO menor valor digitado foi {min(num)} na posição: ', end='')
for mi, v in enumerate(num):
   if min(num) == v:
      print(f'{mi}... ', end='')
