import math

b = int(input('Digite o cateto oposto: '))
c = int(input('Digite o cateto adjacente: '))
hp = math.hypot(math.pow(c, 2), math.pow(b, 2))

print('O valor da hipotenusa é {}'.format(hp))
