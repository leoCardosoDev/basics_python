n1Str = input('Digite um valor: ')
print(type(n1Str))

n1Int = int(input('Digite um número: '))
print(type(n1Int))

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
soma = n1 + n2
print('A soma é = ', soma)

print('A soma entre ', n1, ' e ', n2, ' = ', soma)  # antigo
print('A soma ente {} e {} vale {}'.format(n1, n2, soma))
print('A soma ente {0} e {1} vale {2}'.format(n1, n2, soma))
