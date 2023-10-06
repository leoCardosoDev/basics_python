import math

b = int(input('Digite o cateto oposto: '))
c = int(input('Digite o cateto adjacente: '))
a = math.pow(c, 2) + math.pow(b, 2)
hp = math.hypot(b, c)

print('O valor da hipotenusa é {}'.format(hp))
