from time import sleep

cores = ('\033[m',
         '\033[0;30;41m',
         '\033[0;30;42m',
         '\033[0;30;43m',
         '\033[0;30;44m',
         '\033[0;30;45m',
         '\033[7;30m',
         )

def ajuda(cmd):
    print(cores[5], end='')
    help(cmd)
    print(cores[0], end='')
    sleep(2)

def titulo(msg: str, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg.upper()}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).strip().lower()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)
