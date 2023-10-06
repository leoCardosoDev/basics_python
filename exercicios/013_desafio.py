sa = int(input('Digite seu salario atual? R$ '))
sp = (15 / 100) * sa
sf = sa + sp
print('Seu salário atual é de R$ {}, mas com 15% de aumento ficará em R$ {:.2f}'.format(sa, sf))
