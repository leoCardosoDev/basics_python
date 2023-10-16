def escreva(txt: str):
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(f'  {txt.upper()}')
    print('~' * tamanho)


escreva('Leo Silva')
escreva('Curso de Python no Youtube')
escreva('Aprenda a programar')
escreva('CeV')
