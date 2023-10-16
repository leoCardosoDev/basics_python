from time import sleep
from operator import neg, abs


def contador(inicio, fim, passo):
    passoString = str(passo).replace("-", "")
    print(f'Contagem de {inicio} até {fim} de {passoString} em {passoString}')
    if fim > inicio:
        fim += 1
    else:
        fim -= 1
        if passo > 0:
            passo = neg(passo)
        elif fim < 0:
            passo -= 1
    if fim == 0:
        fim -= fim
    for index in range(inicio, fim, passo):
        print(f'{index} ', end='', flush=True)
        sleep(.5)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
