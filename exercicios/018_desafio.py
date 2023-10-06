import math
a = int(input('Digite um ângulo: '))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)

print('O angulo de {}° tem o valor de seno de {:.1f}, o valor de cosseno {:.1f} e o valor de tangente de {:.1f}'.format(a, s, c, t))
