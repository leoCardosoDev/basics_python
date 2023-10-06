import math
i = float(input('Digite um ângulo: '))
s = math.sin(math.radians(i))
c = math.cos(math.radians(i))
t = math.tan(math.radians(i))

print('O angulo de {}° tem o valor de seno de {:.2f}, o valor de cosseno {:.2f} e o valor de tangente de {:.2f}'.format(i, s, c, t))
