"""
 listas

  listas em python funcional como vetores/matrizes (arrys) em outras linguagnes, com a diferença
  de serem DINAMICO  e tambem de podermos colocar QUALQER tipo de dado.

  linguagens c/java: arrays
  possuem tamanho e tipo de dados fixo;
  ou seja,  nestas linguagens se voce criar um array do tipo int e com tamanho 5, este array
  sera sempre do tipo interio e podera ter SEMPRE no maximo 5 valores.

  ja em python:

  - dinamico: não possui tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
  - qualquer tipo de dados: não possuem tipo de dados fixo; ou seja, podemos colocar qualquer tipo de dado;

  as listas em python são representadas por colchetes: []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['w', 'e', 's', 'l', 'e', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Wesley da Silva Freire')

#podemos facilmente checar se determinado valor esta contido na lista
num = 7
if num in lista4:
    print(f'encontrei o numero {num}')
else:
    print(f'não encontrei o numero {num}')


#podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

# podemos facilemte contar o numero de ocorrencias de um valor em lista
print(lista1.count(1))
print(lista2.count('e'))

#adicionar elementos em listas

"""
para adicionar elementos em listas, ultilizamos a função append
"""