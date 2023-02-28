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
"""
# fazendo import
from collections import OrderedDict

dicionario =OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})