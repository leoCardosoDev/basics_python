nome = str(input('Qual é o seu nome? '))
if nome == 'Leo':
    print('WOW! {}! Que nome bonito!'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Hummm, seu nome é bem popular no Brasil {}.'.format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Olha {}, seu nome é bem normal.'.format(nome))
print('Tenha um bom dia, {}'.format(nome))
