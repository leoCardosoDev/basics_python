sa = int(input('Digite seu salario atual? R$ '))
sf = sa + (sa * 15 / 100)
print('Seu salário atual é de R$ {:.2f}, mas com 15% de aumento ficará em R$ {:.2f}'.format(sa, sf))
