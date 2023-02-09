"""
dicionarios

obs: em algumas linguagem de programação, os dicionarios python são conhecidos
 por mapas.

 dicionarios são coleções do tipo chave/valor.

dicionarios são representados por chave {}.

obs: sobre dicionarios
- chave e valor são separados por dois pontos 'chave:valor;
- tanto chave quanto valor podem ser de qualquer tipo de dado;
- podemos misturar tipos de dados;

#criação de dicionarios
#forma 1 (mais comum)
paises = {'br': 'brasil', 'eua': 'estados unidos', 'py': 'paraguai'}

print(paises)
print(type(paises))

# forma 2 (menos comum)
paises = dict(br = 'brasil', eua = 'estados unidos', py = 'paraguai')

print (paises)
print(type(paises))
"""
paises = {'br': 'brasil', 'eua': 'estados unidos', 'py': 'paraguai'}

#acessando elementos

#froma 1 - acessando via chave, da mesma froma que lista/tupla
print(paises['br'])
print(paises['py'])