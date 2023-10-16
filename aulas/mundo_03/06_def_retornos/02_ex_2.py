def contador(inicio, fim, passo):
    """
    -> Faz uma contagem e mostra na tela
    :param inicio: inicio da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno (void)
    """
    contador = inicio
    while contador <= fim:
        print(f'{contador} ', end='')
        contador += passo
    print()


contador(2, 10, 2)

help(contador)
