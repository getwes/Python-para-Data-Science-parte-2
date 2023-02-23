"""
- conjuntos em qual quer linguagem de programação , estamos fazendo referencia a teoria dos conjuntos
 da matematica.

- aqui no python, os conjuntos são chamados de sets.

dito isto, da mesma froma que na matematica:

- sets (conjuntos) não possuem valores duplicados;
-sets (conjuntos) não possuem valores ordenados;
- valores não são acessados via indice, ou seja, conujuntos não são indexados;

conjuntos são bons para se ultilizar quando precisamos armazenar elementos
mas não nos iumportamos com a ordenação deles. quando não precisamos se preocupar
com chaves, valores e itens duplicados.

os conjuntso (sets) são referenciados em python com chaves {}

diferença entre conjuntos (set) e mapas (dicionarios) em python:
  - um dicionario tem chave/valor;
  - um conjunto tem apenas valor;

  # definindo um conjunto:
# forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) #repare que temos valores repetidos.

print(s)
print(type(s))

#obs: ao criar um conjunto caso seja adiconado um valor ja existente, o mesmo
# sera iginorado sem gerar error e não fara parte do conjunto.

# forma 2 - mais comum

s = ({1, 2, 3, 4, 5, 5})
print(s)
print(type(s))

#set não tem repeti~çao de dados

#podemos verificar se determinado elemento esta contido no conjunto
if 3 in s:
    print('tem o 3')
else:
    print('não tem 3')

# aqui podemos ver que o set pode ser usando em lista, dicionario, conjunto ,tupla 
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 27, 99, 13, 12, 13, 2, 2]

print(set(lista1))
"""
# importante lembrar que, além de não termos valores duplicado não temos ordem

lista = [99, 2, 34, 23, 2, 12, 1,44, 5, 34]
print(f'lista: {lista} com {len(lista)} elemento')

tupla = (99, 2, 34, 23, 2, 12, 1,44, 5, 34)
print(f'tupla: {tupla} com {len(tupla)} elemento')

dicionario = {}.fromkeys ([99, 2, 34, 23, 2, 12, 1,44, 5, 34], 'dict')
print(f'dicionario: {dicionario} com {len(dicionario)} elemento')
conjunto = {99, 2, 34, 23, 2, 12, 1,44, 5, 34}
print(f'conjunto: {conjunto}' com {len(conjunto)} elemento)