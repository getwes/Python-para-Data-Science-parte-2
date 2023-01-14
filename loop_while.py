"""
loop while

forma geral 

while expressão_booleana:
    #execuçaõ do loop

o bloco do while sera repetido enquanto a expressão booleana for verdadeira.

expressão booleada é toda expressão onde o resultado é verdadeiro ou falso.

exemplo:

num = 5

num < 5

#exemplo 1
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1


#obs: em loop while, é importante que cuidemos do criterio de parada para não causar um loop infinito
"""

#exemplo 2
resposta = ''

while resposta != 'sim':
    resposta = input(' ja acabou jessica?')  # enquanto a resposta do usuario não for sim  o rpgrama vai ficar repetindo a perguta diversas vezes.