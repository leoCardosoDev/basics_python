def aumentar(preco, porcem):
    return moeda(preco + (porcem / 100) * preco)


def diminuir(preco, porcem):
    return moeda(preco - (porcem / 100) * preco)


def metade(preco):
    return moeda(preco / 2)


def dobro(preco):
    return moeda(preco * 2)


def moeda(preco: float, moeda='R$'):
    return f'{moeda} {preco:8.2f}'.replace('.', ',')
