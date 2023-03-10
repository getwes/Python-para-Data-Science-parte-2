"""
basicamento é para nomear uma tupla
modulo collection - named tuple

#recap tupla
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tupla[1])

named tuple -> são tuplas, difereciada, onde, especificamos um nome para a mesma e tambem parametros.
"""
# import

from collections import namedtuple

#precisoamos definir o nome e parametros.

#forma 1 - declaração named tuple
#tipo - cachorro
cachorro = namedtuple('cachorro', 'idade raca nome')

#forma 2 - declaração named tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

#forma 3 - declaração named tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#usando
ray = cachorro(idade=2, raca='chow-chow', nome='ray')

print(ray)

#acessando os dados

#forma 1

print(ray[0]) # idade
print(ray[1]) # raça
print(ray[2]) # nome

#forma 2

print(ray.idade) # idade
print(ray.raca) # raça
print(ray.nome) # nome

print(ray.index('chow-chow'))# qual o indice

print(ray.count('chow-chow')) # quantas ocorrencias

#qual quer coisa pesquisar
#https://docs.python.org/3/library/collections.html#collections.namedtuple
