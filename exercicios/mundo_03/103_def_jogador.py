def ficha(nome='<desconhecido>', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


jogador = str(input('Nome do jogador: '))
gols = input('Número de gols: ')
if gols.isnumeric() == False:
    gols = 0

print(ficha(jogador, int(gols)))
