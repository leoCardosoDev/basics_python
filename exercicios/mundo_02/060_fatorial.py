num = int(input('Digite um número: '))
c = num
resultado = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    resultado *= c
    c -= 1
print(f'{resultado}')
