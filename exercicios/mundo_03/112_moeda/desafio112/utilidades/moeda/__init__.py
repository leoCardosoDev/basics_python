def aumentar(numero, porcem, formatado=False):
    if formatado:
        return moedaF(numero + (porcem / 100) * numero)
    else:
        return numero + (porcem / 100) * numero


def diminuir(numero, porcem, formatado=False):
    if formatado:
        return moedaF(numero - (porcem / 100) * numero)
    else:
        return numero - (porcem / 100) * numero


def metade(numero, formatado=False):
    if formatado:
        return moedaF(numero / 2)
    else:
        return numero / 2


def dobro(numero, formatado=False):
    if formatado:
        return moedaF(numero * 2)
    else:
        return numero * 2


def moedaF(numero: float):
    return f'R$ {numero:.2f}'


def resumo(preco, aumento, reducao):
    print('-'*30)
    print(f'    RESUMO DO VALOR   ')
    print('-'*30)

    print(f'{"Preço analizado: ":<4}', end='')
    print(f'{moedaF(preco):>15}', end='')
    print()
    print(f'{"Dobro do preço: ":<4}', end='')
    print(f'{dobro(preco, True):>15}', end='')
    print()
    print(f'{aumento}{"% de aumento: ":<4}', end='')
    print(f'{aumentar(preco, aumento, True):>15}', end='')
    print()
    print(f'{reducao}{"% de redução: ":<4}', end='')
    print(f'{diminuir(preco, reducao, True):>15}', end='')
    print()
