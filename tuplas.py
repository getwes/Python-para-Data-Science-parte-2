"""

tuplas (tuple)
 tuplas são bastante parecidas com listas.

 existem basicamente duas diferenças basicas:

 1 - as tuplas são representadas por parenteses ()

 2 - as tuplas são imutaveis: isso significa que ao se criar uma tupla ela não muda. toda
 operação em uma tupla gera uma nova tupla.
"""

# cuidado 1 : as tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type((tupla1)))

tupla2 = 1, 2, 3, 4, 5, 6, 45, 65, 7, 98, 32, 71 
print(tupla2)

print(type((tupla2)))

#cuidado 2: tuplas com 1 elemento

tupla3 = (4)
print(tupla3)

print(type((tupla3)))

"""
Tupla é um tipo de estrutura de dados utilizada em Python que funciona de modo semelhante a uma lista, entretanto, com a característica principal de ser imutável. Isso significa que quando uma tupla é criada não é possível adicionar, alterar ou remover seus elementos. Geralmente, ela é utilizada para adicionar tipos diferentes de informações, porém, com a quantidade de elementos definidos.

Podemos utilizar uma tupla de dois elementos, por exemplo, para indicar a sigla do estado em uma posição e o nome dele em outra. Portanto, ela é uma boa opção quando queremos trabalhar com informações diferentes em uma mesma variável e quando queremos que esses dados não sofram alterações.

Sua característica de imutabilidade oferece segurança nas informações armazenadas. Por isso, uma das finalidades da tupla é armazenar uma sequência de dados que não será modificada em outras partes do código.

Entretanto, ela não é completamente imutável, pois quando armazena outro objeto, como uma lista, os dados armazenados nesse elemento podem ser modificados. É preciso entender, porém, que nesse caso não é alterado a estrutura da tupla, apenas o conteúdo desse objeto, que é passado por referência.

Imagine que temos uma tupla que contém dois elementos, uma string com o nome de uma pessoa, e uma lista com os nomes de seus filhos. Perceba que a lista de filhos pode e deve sofrer alterações, caso a pessoa tenha um novo filho. Entretanto, a estrutura da tupla não foi alterada, pois ela continua com os mesmos elementos e função.
"""