from desafio115.lib.interface import cabecalho


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo!')


def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('Listar Pessoas')
        print(arquivo.read())
