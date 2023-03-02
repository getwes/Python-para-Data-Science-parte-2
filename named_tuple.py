"""
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

cachorro = namedtuple('cachorro', 'idade raca nome')

#forma 2 - declaração named tuple

cachorro2 = namedtuple('cachorro2', 'idade, raca, nome')
