expressao = str(input('Digite uma expressão: ')).strip()
expressao_aberta = []
expressao_fechada = []

for caracter in expressao:
  if caracter == '(':
    expressao_aberta.append(caracter)
  
  if caracter == ')':
    expressao_fechada.append(caracter)

if len(expressao_aberta) == len(expressao_fechada):
  print('Sua expressão está certa!')
else:
  print('Sua expressão está errada!')
