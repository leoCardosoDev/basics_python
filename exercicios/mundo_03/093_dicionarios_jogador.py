stats = {}
jogador = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador} jogou? '))
gols = []
total = 0

for i in range(0, partidas):
  gol = int(input(f'Quantos gols na partida {i}? '))
  total += gol
  gols.append(gol)

stats['nome'] = jogador
stats['gols'] = gols[:]
stats['total'] = total

for key, values in stats.items():
  print(f'O {key} tem o valor {values}')
print(f'O jogador {jogador} jogou {partidas} partidas.')

for pos, g in enumerate(stats['gols']):
  print(f'Na partida {pos}, fez {g} gols. ')
print(f'Fez um total de {stats["total"]} gols')

