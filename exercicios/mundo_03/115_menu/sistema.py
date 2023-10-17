from desafio115.lib.interface import *
from time import sleep

while True:
    resposta = menu(
        ['Listar Pessoas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Listar Pessoas')
    elif resposta == 2:
        cabecalho('Cadastrar Nova Pessoa')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo')
        break
    else:
        print('\033[1;31mErro! Digite uma opção válida!\033[m')
    sleep(2)
