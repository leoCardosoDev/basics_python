num = int(input('Digite um número: '))
resultado = 1
while num > 1:
    resultado *= num
    num -= 1
print(f'O fatorial de {resultado}')
