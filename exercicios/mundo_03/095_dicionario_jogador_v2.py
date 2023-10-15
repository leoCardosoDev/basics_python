stats = {}
jogadores = []
gols = []
total = 0

while True:
    nome = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for i in range(0, partidas):
        gol = int(input(f'Quantos gols na {i+1}ª partida? '))
        total += gol
        gols.insert(i, gol)
    stats['nome'] = nome
    stats['gols'] = gols
    stats['total'] = total
    jogadores.append(stats.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar not in 'S':
        print(f'{"Cod:":<4} {"Nome:":<10} {"gols":<5} {"total":>10}')
        for pos, value in enumerate(jogadores):
            print(f'{pos} => {value["nome"]} => {value["gols"]} => {value["total"]}')
        while True:
            dados = int(input('Mostrar dados de qual jogador? '))
            if dados == 999:
                break
            if 0 <= dados < len(jogadores):
                print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]}')
                for pos, g in enumerate(jogadores[dados]["gols"]):
                    print(f'No jogo {pos} fez {g} gols')
            else:
                print('Número inválido! Tente novamente')
        break
