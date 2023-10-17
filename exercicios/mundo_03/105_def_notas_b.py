def notas(*nota, sit=False):
  ficha = dict()

  ficha['total'] = len(nota)
  ficha['maior'] = max(nota)
  ficha['menor'] = min(nota)
  ficha['media'] = sum(nota) / len(nota)
  if sit:
    if ficha['media'] >= 7.5:
      ficha['situacao'] = 'BOA'
    elif ficha['media'] >= 5:
      ficha['situacao'] = 'RAZOAVÉL'
    else: 
      ficha['situacao'] = 'RUIM'
  return ficha
  

resposta = notas(6.4, 6.4, 6.4, 6.4, sit=True)
print(resposta)
