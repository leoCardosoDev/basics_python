p = float(input('Digite o valor do produto: R$ '))
pf = p - ((5 / p) * 100)
print('O produto custa R$ {}, mas você obteve 5% de desconto e o valor final ficou em R$ {:.2f}'.format(p, pf))
