"""
modulo collections - default dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# recap dicionarios

dicionario = {'curso': 'programação em python: essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # ??? key error

default dict -> ao criar um dicionario ultilizando-o, nos informamos um valor default,
podendo utilizar um lambda para isso. este valor sera utilizado sempre que não houver
um valor definido. caso tentemos acessar uma chve que não existe, essa chave sera 
criada e o valor default sera attribuido.

obs: lambedas são funçoes sem nome, que podem ou não receber parametros de entrada
e retornar valores.
"""
#fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'programação em pythn: essencial'
print(dicionario)

print(dicionario['outro']) # key error no dicionario comum, mas aqui não.

print(dicionario)