import math

b = int(input('Digite o cateto oposto: '))
c = int(input('Digite o cateto adjacente: '))
hp = math.hypot(b, c)


print('O valor da hipotenusa é {}'.format(hp))
