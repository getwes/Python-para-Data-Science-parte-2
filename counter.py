"""
modulo collections - counter (contador)

collections - high-performance container datetypes

counter - recebe um interavel como parametro e cria um objeto do tipo collections counter que é parecido
com um dicionario,contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento.

# ultilizando o counter
#realizando
from collections import Counter

#exemplo 1
# podemos ultilizar qualquer interavel, aqui usando uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34, 100]
# ultilizando o counter
res = Counter(lista)

print(type(res))
print(res)

#Counter({5: 6, 1: 5, 3: 5, 2: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1, 100: 1})

#veja que, para cada elemento da lista, o counter criou uma chave e colocou como valor a quantidade de ocorrencias.

"""
