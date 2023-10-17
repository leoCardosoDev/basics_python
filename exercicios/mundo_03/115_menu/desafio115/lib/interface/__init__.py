def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(
                '\n\033[1;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(txt: str):
    print(linha())
    print(txt.upper().center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[m - \033[0;33m{item}\033[m')
        c += 1
    print(linha())
    opcoes = leiaInt('\033[1;32mSuas Opção: \033[m')
    return opcoes
