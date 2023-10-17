from desafio111.utilidades import dado


def resumo(preco, aumento, reducao):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analizado: \t{dado.moeda(preco)}')
    print('-'*30)
    print(f'Dobro do preço: \t{dado.dobro(preco, True)}')
    print(f'{aumento}% de aumento: \t{dado.aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{dado.diminuir(preco, reducao, True)}')
