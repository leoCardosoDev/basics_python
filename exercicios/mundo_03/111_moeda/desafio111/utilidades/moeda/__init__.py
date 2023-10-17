from desafio111.utilidades import dado


def resumo(preco, aumento, reducao):
    print('-'*30)
    print(f'    RESUMO DO VALOR   ')
    print('-'*30)

    print(f'{"Preço analizado: ":<4}', end='')
    print(f'{dado.moeda(preco):>15}', end='')
    print()
    print(f'{"Dobro do preço: ":<4}', end='')
    print(f'{dado.dobro(preco, True):>15}', end='')
    print()
    print(f'{aumento}{"% de aumento: ":<4}', end='')
    print(f'{dado.aumentar(preco, aumento, True):>15}', end='')
    print()
    print(f'{reducao}{"% de redução: ":<4}', end='')
    print(f'{dado.diminuir(preco, reducao, True):>15}', end='')
    print()
