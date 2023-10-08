dec = int(input('Digite um número inteiro: '))
base = int(
    input('Digite 1 para converter em binário: 2 para OCTAL e 3 para hexadecimal '))

if base == 1:
    # result = bin(dec)
    result = format(dec, 'b')
elif base == 2:
    result = oct(dec)
elif base == 3:
    result = hex(dec)
else:
    result = base
print(result)
