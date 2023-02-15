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

#acessando elementos

#froma 1 - acessando via chave, da mesma froma que lista/tupla
print(paises['br'])
#print(paises['ru'])

 #obs: caso tentamos fazer um acesso ultilizando uma chave que não existe, teremoa o erro keyerror

 #forma 2 - acesso via get - recomendado

 paises = {'br': 'brasil', 'eua': 'estados unidos', 'py': 'paraguai'}

print(paises.get('br'))
print(paises.get('py'))
print(paises.get('ru'))


# caso o get não encontre o objeto com a chave informada sera retornado o valor none e não sera gerado keyerror
pais = paises.get('ru',)

if pais:
    print(f'encontrei o pais {pais}')

else:
    print('não encontrei o pais')

_____________________________________________________
# podemos definir um valor padrão para caso não encontremos o objseto com a chave informada
    pais = paises.get('ru', 'não contrado')
    
print(f'encontrei o pais {pais}')


paises = {'br': 'brasil', 'eua': 'estados unidos', 'py': 'paraguai'}
# podemos verificar se determinada chave se encontra em um dicionario
print('br' in paises)
print('ru' in paises)
print('estados unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']


# podemos ultilizar qualquer tipo de dados (int, float, string, bolean), inclusive lista, tupla dicionario, como chaves
#de dicionarios.

# tupla é bom para se usar como chave pois são imutavel não pode ser alterado durante o codigo
# tuplas por exemplo são bastabte interessantes de serem utilizadas como chave de dicionario, pois as mesmas
#são imutaveis

localidades = {
    (35.6895, 39.6917): 'escritorio em tokio',
    (40.7128, 74.0060): 'escritorio em nova york',
    (37.7749, 122.4194): 'escritorio em são paulo',
}
print(localidades)
print(type(localidades))

# adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

#forma 1 - mais comum

receita['abr'] = 350

print(receita)

#forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado)# receita.update({'mai': 500})
print(receita)

# atualizando dados em um dicionario

# forma 1

receita['mai'] = 550
print(receita)

# forma 2

receita.update({'mai': 600})
print(receita)

# conclusão 1: a forma de adicionar novos elementos ou atualizar dados em um dicionarios é a mesma.
# conclusão 2: em dicionariso, não podemos ter chaves repetidas.

"""
# remover dados de um dicionario]
receita = {'jan': 100, 'fev': 120, 'mar': 300}
# forma 1 - forma mais comum
ret = receita.pop('mar')
print(ret)

print(receita)
# obs 1: aqui precisamos sempre informar a chave, e casdo não encotre o elemento, um keyerror é retornado.
# obs 2: ao removermos um objeto, o valor deste objeto é sempre retornado.

# froma 2
# del de deletar
del receita['fev']
print(receita)

# se a chave não existir sera gerado um keyerror
# obs: neste caso o valor removiodo não é retornado.