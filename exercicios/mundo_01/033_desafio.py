n1 = int(input('DIgite um número: '))
n2 = int(input('DIgite outro número: '))
n3 = int(input('DIgite outro número: '))

maior = n1
menor = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor digitado foi: {} é menor digitado'.format(menor))
print('O maior valor digitado foi: {} é menor digitado'.format(maior))
