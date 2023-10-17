def aumentar(numero, porcem):
    return moeda(numero + (porcem / 100) * numero)


def diminuir(numero, porcem):
    return moeda(numero - (porcem / 100) * numero)


def metade(numero):
    return moeda(numero / 2)


def dobro(numero):
    return moeda(numero * 2)


def moeda(numero: float):
    return f'R$ {numero:.2f}'
