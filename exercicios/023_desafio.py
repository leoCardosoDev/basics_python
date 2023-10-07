entrada = int(input('Digite um número de 0 a 9999: '))
num = int(entrada)
alg = str(entrada)
print(len(alg))
unidade = alg[3::1]
dezena = alg[2::2]
centena = alg[1::3]
milhar = alg[0::4]
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
print('----' * 10)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade com número: {}'.format(u))
print('Dezena com número: {}'.format(d))
print('Centena com número: {}'.format(c))
print('Milhar com número: {}'.format(m))
