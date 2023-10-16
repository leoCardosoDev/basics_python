from time import sleep


def contador(i, f, p):
    ps = str(p).replace("-", "")
    print(f'Contagem de {i} até {f} de {ps} em {ps}')
    if f > 0:
       f += 1
    for index in range(i, f, p):
        print(f'{index} ', end='')
    sleep(.5)
    print()


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
