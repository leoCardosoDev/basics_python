dec = int(input('Digite um número inteiro: '))
base = int(input('''
Digite:
[1] para converter em binário
[2] para converter em OCTAL
[3] para converter em hexadecimal
'''))

if base == 1:
    result = f'{bin(dec)[2:]}'
elif base == 2:
    result = f'{oct(dec)[2:]}'
elif base == 3:
    result = f'{hex(dec)[2:]}'
else:
    result = base
print(result)
