dias = int(input('Quantos dias ele foi alugado? '))
km = float(input('Qual a quantidade de KM pecorridos? '))
total = (dias * 60) + (km * 0.15)

print('O total a pagar é R$ {:.2f}'.format(total))
