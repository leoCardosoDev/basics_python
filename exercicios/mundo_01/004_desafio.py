entrada = input('Digite um ou 3 caracteres: ')
print('É um númemo? {}'.format(entrada.isnumeric()))
print('Contém apenas letra? {}'.format(entrada.isalpha()))
print('Contém letras e números? {}'.format(entrada.isalnum()))
