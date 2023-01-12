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

for letra in nome:
    print(letra)

#exemplo de for 2 (interando sobre uma lista)
for numero in lista:
    print(numero)

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
for numero in range(1, 10):
    print(numero)
