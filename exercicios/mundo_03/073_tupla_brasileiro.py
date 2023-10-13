times = 'Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Fluminense', 'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Cuiabá', 'Internacional', 'Corinthians', 'Santos', 'Cruzeiro', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'América-MG'

print('Lista dos times do Brasileirão: ', end='')
print(times)

print('-=' * 40)
print('Os 5 primeiros: ', end='')
print(times[:5])

print('-=' * 40)
print('Os quatros últimos: ', end='')
print(sorted(times[-4:]))

print('-=' * 40)
print('Times em ordem alfabetica: ', end='')
print(sorted(times))

print('-=' * 40)
print(f'O time {times[9]} está na {times.index("São Paulo")+1}º posição: ')
