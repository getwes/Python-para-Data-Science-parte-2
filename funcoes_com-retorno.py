"""
funções com retorno

refatorar é fazer modificaçoes que melhorem nosso codidos

numeros = [1, 2, 3]

ret_pop = numeros.pop()
print(f'retorno de pop: {ret_pop}')

ret_print = print(numeros)

print(f'retorno de print: {ret_print}')

obs: em python quando uma função não retorna nenhum valor, o retorno é none
obs: funçoes python que rentornam valor devem retornar estes valores com a palavra reservada return
obs: nçao precisamos necessariamente criar umas vaariavel para receber o retorno
 de uma função. podemos passar a execução da função para outras funções.

ef quadrado_de_7():
    return 7 * 7
#criamos uma variavel para receber o retorno da função
ret = quadrado_de_7()

print(f'retorno de {ret}')
 # podemos ultlizar dessa forma tambem e podemos fazer somas e atribuições dentro das chaves
print(f'retorno: {quadrado_de_7()}') 

# refatorando a primera função

def diz_oi():
    return 'oi, '

alguem = 'pedro!'

print(diz_oi() + alguem)

obs: sobre a palavra reservada return

1 - ela finaliza a função, ou seja, ela sai da execução da função;
2 - podemos ter, em uma função, diferentes returns;
3 - podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;

#exemplos 1 - ela finaliza a função, ou seja, ela sai da execução da função;

def diz_oi():
    print('estou sendo executado antes do retorno...')
    return 'oi! '
    print('estou sendo executado apos o retorno...')

print(diz_oi())

# exemplo 2 - podemos ter, em uma função, diferentes returns;

def nova_funcao():# se varaivel for igual a true retorna 4 se variavel for igual a none retorna 3.2, caso não seja nem uma das duas retorna 'b'
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

#exemplo 3 - podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;

def outra_fucao():
    return 2, 3, 4, 5


#num1, num2, num3, num4 = outra_fucao()

#print(num1, num2, num3, num4)

print(outra_fucao())
print(type(outra_fucao))

# vamos criar uma função para jogar a moeda
#pacotes
from random import random

def joga_moeda():
    #gera um numero pseudo- randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'

#refatorando
#def joga_moeda():
    #gera um numero pseudo- randômico entre 0 e 1
   # if random() > 0.5:
      #  return 'cara'
   # return 'coroa'


print(joga_moeda())
"""

#erros comuns na utilização de retorno, que na verdade nem é erro, mas sim codificação desnecessarias.


def eh_impar():
    numero = 5
    if numero % 2 != 0: #se numero modulo de 2 for diferente de 0
        return True
    else: # não tem necessidade de por o else aqui
        return False
    
print(eh_impar())