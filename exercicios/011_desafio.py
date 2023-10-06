alt = float(input('Digite a altura: '))
lag = float(input('Digite a largura: '))

lt = (alt * lag) / (2**2)
print('Você precisará de {:.2f}lt de tintas para pintar a área'.format(lt))
