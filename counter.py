"""
modulo collections - counter (contador)

collections - high-performance container datetypes

counter - recebe um interavel como parametro e cria um objeto do tipo collections counter que é parecido
com um dicionario,contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento.

"""
# ultilizando o counter
#realizando
from collections import Counter
# podemos ultilizar qualquer interavel, aqui usando uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34, 100]
# ultilizando o counter
res = Counter(lista)

print(type(res))
print(res)