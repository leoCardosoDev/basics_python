from math import sqrt
n = int(input('Digite um número: '))
if n == 2:
    print(f'{n} é um número primo')
if n > 1:
    for p in range(3, int(sqrt(n)) + 1, 2):
        if n % p == 1:
            print(f'{n} é um número primo')
        else:
            print(f'{n} não é um número primo')
else:
    print(f'{n} não é um número primo')

# Errado
