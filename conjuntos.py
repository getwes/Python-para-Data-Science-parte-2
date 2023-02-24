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

# importante lembrar que, além de não termos valores duplicado não temos ordem
#listas aceitam valores duplicado então temos 10 elelemtos
lista = [99, 2, 34, 23, 2, 12, 1,44, 5, 34]
print(f'lista: {lista} com {len(lista)} elemento') 

#tupla aceitam valores duplicado então temos 10 elelemtos
tupla = (99, 2, 34, 23, 2, 12, 1,44, 5, 34)
print(f'tupla: {tupla} com {len(tupla)} elemento')
#dicionario não aceitam chaves duplicadas, então temos 8 elelemtos
dicionario = {}.fromkeys ([99, 2, 34, 23, 2, 12, 1,44, 5, 34], 'dict')
print(f'dicionario: {dicionario} com {len(dicionario)} elemento')
#conjunto não aceitam valores duplicado, então temos 8 elelemtos
conjunto = {99, 2, 34, 23, 2, 12, 1,44, 5, 34}
print(f'conjunto: {conjunto} com {len(conjunto)} elemento')

#assim como todos outros conjuntos python podemos colocar tipos de dados misturados em sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

for valor in s:
    print(valor)

#usos interessantes com sets

# imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes
#informam manualmente a ciade de onde vieram.

#nós adicionamos cada cidade em uma lista python, ja que em uma lista podemos adicionar novos elementos
#e ter repetição.

cidades = ['belo horizonte', 'são paulo', 'campo grande', 'cuiaba', 'campo grande', 'são paulo', 'cuiaba']
print(cidades)
print(len(cidades))

#agora precisamos saber quantas cidades distintas, ou seja, unicas, temos.

# oque voce faria? faria um loop na lista??

#podemos ultilizar o set para isso:

print(len(set(cidades)))

# adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4) #duplicidade não gera erro. simplesmenrte é iginorado e não adicionado
print(s)


# remover elementos em um conjunto
s = {1, 2, 3}
print(s)

#forma 1

s.remove(3) #não é indice informamos o valor a ser removido 
print(s)

#obs: caso o valor não seja encontrado seja gerado o erro keyerror. nem um valor é retornado

#forma 2

s.discard(2)
print(s)

#obs: se o valor não for encotnrado nem um erro é gerado

s = {1, 2, 3}
print(s)
# copiando um conjunto para outro..

#forma 1 - deep copy
novo = s.copy()
print(novo)

novo.add(4) 

print(novo)
print(s)

s = {1, 2, 3}
print(s)

# forma 2 -shallow copy

novo = s

novo.add(4)

print(novo)
print(s)

s = {1, 2, 3}
print(s)

# podemos remover todos os itens de um conjunto

s.clear()
print(s)

#precisamos gerar um conjunto com nomes de estudantes unicos

# forma 1 - ultilizando union
#union é união

unicos1 = estudante_python.union(estudante_java) # mesmo que inverter os estrudantes e seu curso ira dar o mesmo resultado.
print(unicos1)

# forma 2 - ultilizando o carcter pipe |

unicos2 = estudante_python | estudante_java
print(unicos2)

#veja que alguns alunos que estudam python tambem estudam java.

#gerar um conjunto de estudantes que estão em ambos os cursos

#forma 1 - ultilizando interrsection
# importante
ambos1 = estudante_python.intersection(estudante_java)
print(ambos1)

#forma 2 - ultilizando o & 

ambos2 = estudante_python & estudante_java
print(ambos2)
"""
# metodos matematicos de conjunto

#imaigne que temos dois conjuntos um contendo estudantes do curso python e um
# contendo estudantes do curso java.

estudante_python = {'marcos', 'patricia', 'ellen', 'pedro', 'julia', 'guilherme'}
estudante_java = {'fernando', 'gustavo', 'julia', 'ana', 'patricia'}

