"""
  modulo collection: ordered dict

  # em dicionario, a ordem de inserção dos elementos não é garatinda.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

#print(dicionario.keys())
#print(dicionario.values())
#print(dicionario.items())
#python library

ordereddict -> é um dicionario, que nos garante a ordem de inserção dos elementos.

# fazendo import
from collections import OrderedDict

dicionario =OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""
# entendendo a diferença entre dict e ordered dict

# dicionanrios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print( dict1 == dict2) #True -> ja que a ordem dos elementos não importa para o dicionario

#ordered dict

from collections import OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print( odict1 == odict2) # false -> ja que a ordem dos elementos importa para o ordereddict

#https://docs.python.org/3/library/collections.html#collections.OrderedDict