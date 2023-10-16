from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        p *= -1
    if passo == 0:
        passo = 1
    sleep(.5)
    print(f'Contagem de {inicio} até o {fim}, de {passo} em {passo}')
    contador = inicio
    if inicio < fim:
        while contador <= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(.3)
            contador += passo
        print()
    else:
        while contador >= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(.3)
            contador -= passo
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
