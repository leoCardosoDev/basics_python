def aumentar(preco, porcem, formatado=False):
    resposta = preco + (porcem / 100) * preco
    return resposta if formatado else moeda(preco + (porcem / 100) * preco)


def diminuir(preco, porcem, formatado=False):
    resposta = preco - (porcem / 100) * preco
    return resposta if formatado else moeda(preco - (porcem / 100) * preco)


def metade(preco, formatado=False):
    resposta = preco / 2
    return resposta if formatado else moeda(preco / 2)


def dobro(preco, formatado=False):
    resposta = preco * 2
    return resposta if formatado else moeda(preco * 2)


def moeda(preco: float):
    return f'{moeda} {preco:8.2f}'.replace('.', ',')
