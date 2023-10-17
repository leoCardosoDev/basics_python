from desafio112.utilidades import moeda
from desafio112.utilidades import dado

preco = dado.leiaDinheiro('Digite o preço R$: ')
moeda.resumo(preco, 80, 35)
