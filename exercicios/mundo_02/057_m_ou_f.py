g = str(input('Qual o seu Sexo? [M/F]: ')).strip().upper()
while g != 'M' and g != 'F':
    g = str(input('Você digitou errado! Tenta os valores M ou F: ')).strip().upper()
print('FIM')
