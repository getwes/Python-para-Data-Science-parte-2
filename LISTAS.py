"""
 listas

  listas em python funcional como vetores/matrizes (arrys) em outras linguagnes, com a diferença
  de serem DINAMICO  e tambem de podermos colocar QUALQER tipo de dado.

  linguagens c/java: arrays
  possuem tamanho e tipo de dados fixo;
  ou seja,  nestas linguagens se voce criar um array do tipo int e com tamanho 5, este array
  sera sempre do tipo interio e podera ter SEMPRE no maximo 5 valores.

  ja em python:

  - dinamico: não possui tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
  - qualquer tipo de dados: não possuem tipo de dados fixo; ou seja, podemos colocar qualquer tipo de dado;

  as listas em python são representadas por colchetes: []

  type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['w', 'e', 's', 'l', 'e', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Wesley da Silva Freire')


  #podemos facilmente checar se determinado valor esta contido na lista
num = 7
if num in lista4:
    print(f'encontrei o numero {num}')
else:
    print(f'não encontrei o numero {num}')


#podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

# podemos facilemte contar o numero de ocorrencias de um valor em lista
print(lista1.count(1))
print(lista2.count('e'))

#adicionar elementos em listas


para adicionar elementos em listas, ultilizamos a função append



lista1.append(100)
print(lista1)

#obs: com append, nos so conseguimos adcicionar 1 elemento por vez
#forma errada lista.append(12, 34, 56)

lista1.append([8, 3, 1]) # coloca a lista como elemento unico (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('encontrei a lista')
else:
    print('não encontrei a lista')

if 100 in lista1:
    print('achei')
else:
    print('não achei')

lista1.extend([123, 44, 67]) # coloca cada elemento da lista como valor adicional á lista
print(lista1)

# podemos inserir um novo elemento na lista informando a posição do indice
#obs: isso não substitui o valor inicial. o mesmo sera deslocado para a direita da lista.
lista1.insert(2, 'novo valor')
print(lista1)
# podemos facilmente juntar duas listas

#lista6 = lista1 + lista2
lista1.extend(lista2) # o extend tambem serve para fazer concatenação de listas e strings
print(lista1)

# a contatenção não serve a penas para numeros serve tambem para strings ou listas.

#podemos facimente inverter uma lista
#froma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)


#forma 2
print(lista1[::-1])
print(lista2[::-1])

# copiar uma lista

lista6 = lista2.copy()
print(lista6)

lista6.sort()
print(lista6)

#podemos contar quantos elementos existem dentro da lista
print(len(lista1))

#podemos facilmente remover o ultimo elemento de uma lista
# obs: o pop não somente remove o ultimo lelemento mas tambem o retorna
print(lista5)
lista5.pop()
print(lista5)

# podemos remover um elemento pelo indice
#obs os elementos a direita deste indicee serão deslocados para a esquerda.
#obs se não houver elemento no indice informado, rteremos o erro indexerror.
print(lista5)
lista5.pop(2)
print(lista5)

# podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# podemos facilmente repetir elementos em uma lista
nova =[1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

#podemos facilmente uma string para uma lista
#exemplo 1

curso = 'programação em python: essencial'
print(curso)
curso = curso.split()
print(curso) 
#obs: por padrão, o split separa os elementento da lista pelo espaço entre elas.

#exemplo 2
curso ='programação,em,python: ,essencial'
print(curso)
curso = curso.split(',') # o sinal de ',' mostra que o padrão não é o espaço e sim separado pelas virgulas.
print(curso)

 # convertendo  uma lista em uma string
 
lista6 = ['progrmação', 'em', 'python:', 'essencial']
print(lista6)

# abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e transforma em uma strings
curso = ' '.join(lista6)
print(curso)
# abaixo estamos falando : pega a lista6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6) # pega essa string para mim e entre cada palavra coloca um '$' entre elas.
print(curso)

# podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'wes', 'd', [1, 2, 3], 4564936657]

print(lista6)
print(type(lista6))

#interando sobre listas 

#exemplo 1 - ultilizado for
soma = 0
for elemento in lista4: #para cada elemento nesta lista imprima cada um para min.
    print(elemento)
    soma = soma + elemento
    print(soma)

soma = ''
for elemento in lista2: 
    soma = soma + elemento
print(soma)

#exemplo 2 - ultilizado while

carrinho = []
produto = ''

while produto != 'sair':
    print("adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

    # ultilizando variaveis em listas
numero = [1, 2, 3, 4, 5]
print(numero)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# fazemos acesso aos elementos de forma indexadas
#            0         1        2         3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

#fazer acesso aos elementos de forma indexado inversa
# para entender melhoir o indice negativo, pense na lista como um circulo, onde
#o final de um eleemento esta ligado ao inicio da lista

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

#listas aceitam valres repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# outros metodos não tão importantes mas tambem uteis

#encontrar o indice de um eleemtno na lista

numeros = [5, 6, 7, 8, 9, 10]

#em qual indice da lista esta o valor 6?
print(numeros.index(6))

#em qual indice da lista esta o valor 9?
print(numeros.index(9))

#obs: caso não tenha este elelemto na lista, será apresentado erro

print(numeros.index(5))# retorna o indice do priomenro elemento encontrado

# podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1)) # buscando a partir do indice 1
print(numeros.index(5, 2)) # buscando a partir do indice 2
# caso não tenha o elemento sera apontado um erro

#podemos  fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))

#exemplo teste
mercado = ['arroz', 'carne', 'ps4', 'xbox', 'tv', 'batata']

print(mercado.index('batata'))

#revisar slicing 

#lista[inicio:fim;passo]
#range(inicio:fim:passo)

#trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:]) # iniciando no indice 1 e pegando todos os elementos restantes
#posso pedir para pegar todos os indices usando ::
# podemos usar numeros negativos tambem -1, -2, -3

#trabalhando com slice de lista com o parametro 'fim'

print(lista[:2])# começa em 0, pega até o indice 2 - 1

print(lista[:4])# começa em 0, pega até o indice 4 - 1

print(lista[1:3])# começa em 1, pega até o indice 3 - 1

#trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2])# começa em 1, vai ate o final de 2 em 2

print(lista[::2])# começa em 0, vai ate o final de 2 em 2

