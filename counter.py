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

#exemplo 2
print(Counter('wesley da silva freire'))
#Counter({'e': 4, ' ': 3, 's': 2, 'l': 2, 'a': 2, 'i': 2, 'r': 2, 'w': 1, 'y': 1, 'd': 1, 'v': 1, 'f': 1})

"""
from collections import Counter

# exmplo 3

texto = """
Um breve comentário antes de começarmos: um Jupyter Notebook com todos os códigos usados neste tutorial está disponível neste repositório do GitHub. Reproduzir os códigos enquanto lê este artigo é altamente recomendado!
O banco de dados e os códigos SQL usados aqui são todos provenientes da minha série Introduction to SQL (Introdução ao SQL) publicada (em inglês) no site Towards Data Science (entre em contato se tiver algum problema para visualizar os artigos e eu enviarei um link para que eles possam ser acessados gratuitamente).
Se não está acostumado com SQL e com os conceitos subjacentes aos bancos de dados relacionais, eu indicaria essa série (além disso, é claro que há uma enorme quantidade de artigos excelentes disponíveis aqui no freeCodeCamp!)
"""

palavras = texto.split()

#print(type(palavras))

#print(palavras)

res = Counter(palavras)

print(res)