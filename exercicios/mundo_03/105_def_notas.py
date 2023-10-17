def notas(*nota, sit=False):
  ficha = {}
  todas = []
  soma = media = total = 0

  for n in nota:
    total += 1
    soma += n
    todas.append(n)

  maior = max(todas)
  menor = min(todas)
  media = soma / total
 
  ficha['total'] = total
  ficha['maior'] = maior
  ficha['menor'] = menor
  ficha['media'] = media
  if sit:
    if media > 7.5:
      ficha['situacao'] = 'BOA'
    elif media > 6.5:
      ficha['situacao'] = 'RAZOAVÉL'
    else: 
      ficha['situacao'] = 'RUIM'
  return ficha
  

resposta = notas(6.6, 6.6, 6.6, 6.6, sit=True)
print(resposta)
