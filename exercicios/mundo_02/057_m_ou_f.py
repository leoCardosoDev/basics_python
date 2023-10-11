g = str(input('Qual o seu Sexo? [M/F]: ')).strip().upper()[0]
while g != 'M' and g != 'F':
    g = str(input('Você digitou errado! Tenta os valores M ou F: ')).strip().upper()
print('FIM')

# while g not in 'MmFf': // solução com python
