def area(largura, comprimento):
  a = largura * comprimento
  print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {a:.1f}m²')


largura = float(input('LARGURA (m²): '))
comprimento = float(input('COMPRIMENTO (m²): '))

area(largura, comprimento)
