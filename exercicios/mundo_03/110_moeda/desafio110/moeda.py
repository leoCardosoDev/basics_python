def aumentar(preco, porcem, formatado=False):
    resposta = preco + (porcem / 100) * preco
    return resposta if formatado is False else moeda(preco + (porcem / 100) * preco)


def diminuir(preco, porcem, formatado=False):
    resposta = preco - (porcem / 100) * preco
    return resposta if formatado is False else moeda(preco - (porcem / 100) * preco)


def metade(preco, formatado=False):
    resposta = preco / 2
    return resposta if formatado is False else moeda(preco / 2)


def dobro(preco, formatado=False):
    resposta = preco * 2
    return resposta if formatado is False else moeda(preco * 2)


def moeda(preco: float, moeda="R$"):
    return f'{moeda} {preco:8.2f}'.replace('.', ',')


def resumo(preco, aumento, reducao):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analizado: \t{moeda(preco)}')
    print('-'*30)
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')
