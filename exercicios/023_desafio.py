num = input(str('Digite um número de 0 a 9999: '))
print(len(num))
unidade = num[3::1]
dezena = num[2::2]
centena = num[1::3]
milhar = num[0::4]
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
