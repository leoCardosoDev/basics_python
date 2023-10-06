n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoInteira = n1 // n2
exponeciacao = n1 ** n2

print('A soma é = {}, a subtração é = {} , a multiplicação é = {},'.format(
    soma, subtracao, multiplicacao), end=' ')
print('a divisão é = {:.3f}, a divisão inteira = {} a exponeciação é {}'.format(
    divisao, divisaoInteira, exponeciacao))

print('A soma é = {}, a subtração é = {} , a multiplicação é = {},\n a divisão é = {:.3f}, a divisão inteira = {} a exponeciação é {}'.format(
    soma, subtracao, multiplicacao, divisao, divisaoInteira, exponeciacao))
