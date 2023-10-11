num2 = int(input('Digite um inteiro: '))
c = num2
resultado = 1
for r in range(num2, 0, -1):
    print(f'{r}', end='')
    print(f' x ' if r > 1 else ' = ', end='')
    resultado *= r
print(f'{resultado}')
