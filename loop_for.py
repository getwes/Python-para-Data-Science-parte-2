""""
Loop for

Loop -> Estrutura de repetição
for -> uma dessas estruturas

for item in interavel:
    //execução do loop

ultilizamos loops para interar sobre sequencia ou sobre valores iteraveis

exemplos  de interáveis:
string
nome = 'geek university'
lista

lista = [1, 3, 5, 7, 9]
range
numeros = range(1, 10)
"""
nome = 'wesley'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # temos que transformar em uma lista

# exemplo de for 1 (interando em uma string)

#for letra in nome:
    #print(letra)

#exemplo de for 2 (interando sobre uma lista)
#for numero in lista:
   # print(numero)

#exemplo de for 3 (intnerando sobre um range)
""""
range(valor_inicial, valor_final)

obeservação: o valor final não é inclusive.

nome = wesley freire
nome[0:6] vai retornar wesley
nome[8:13] vai retornar o freire
mesmo que ultrapasse a quantidade de caracteres o valor vai ser o mesmo 
exemplo [8:14] ou 15 etc 
"""
#for numero in range(1, 10):
   # print(numero)

"""
    enumerate:
   (0, 'w') (1, 'e') (2, 's') etc

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

observação: quando não precisamos de valor, podemos descartá-lo ultilizando um underline (_)

for i, v in enumerate(nome):
    print(nome[i])

qtd = 5
qtd = int(input('quantas vezes esse looop deve rodar?'))
soma = 0
for n in range(1, qtd+1):
    #print(f'imprimindo {n}')
     num = int(input(f'informe o {n}/{qtd} valor: '))
     soma = soma + num
print(f'a soma é {soma}')

nome = 'wesley freire'

for letra in nome:
    print(letra, end='') #end='' serve para juntar todas as letras em uma linha

# ctrl + botão direito encima de print aparece a lista help 

tabela de emojis unicode
"""
# original: U+1F60D
# modificado: