r1 = int(input('Digite o comprimento de uma reta: '))
r2 = int(input('Digite o comprimento de outra reta: '))
r3 = int(input('Digite o comprimento de outra reta: '))

if (r1+r2) > r3 and (r2+r3) > r1 and (r1+r3) > r2:
    print('O triangulo pode ser feito')
else:
    print('O triangulo não pode ser feito')
