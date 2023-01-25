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

print(lista5)
lista5.pop()
print(lista5)
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['w', 'e', 's', 'l', 'e', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Wesley da Silva Freire')

