def aumentar(numero, porcem, formatado=False):
    if formatado:
        return moeda(numero + (porcem / 100) * numero)
    else:
        return numero + (porcem / 100) * numero


def diminuir(numero, porcem, formatado=False):
    if formatado:
        return moeda(numero - (porcem / 100) * numero)
    else:
        return numero - (porcem / 100) * numero


def metade(numero, formatado=False):
    if formatado:
        return moeda(numero / 2)
    else:
        return numero / 2


def dobro(numero, formatado=False):
    if formatado:
        return moeda(numero * 2)
    else:
        return numero * 2


def moeda(numero: float):
    return f'R$ {numero:.2f}'
