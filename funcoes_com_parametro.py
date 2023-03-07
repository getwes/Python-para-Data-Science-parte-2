"""
funções com parametro (de entrada)

- funções que recebem dados para serem processados dentro da mesma;

se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

se a gente pensar em uma função, ja sabemos que temos funções que:
- não possuem entrada;
- não  possuem saida;
- possuem entrada mas não possuem saida;
- não possuem entrada mas possuem saida;
- possuem entrada e saida;

#refatorando uma função

def quadrado(numero):
    #return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(quadrado()) # typeError precisamos de um parametro dentro das ()

#refatorando a função

def cantar_parabens(aniversariante):
    print('parabens para você')
    print('nesta data querida')
    print('muitas felicidades')
    print(f'viva o {aniversariante}!')

cantar_parabens('renan')

# funões podem ter n parametros de entrada. ou seja, podemos receber como entrada
#em uma função quantos parametros forem necessarios. eles são separados por virgula.

#exemplos
from collections import Counter
def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'wesley '))
print(outra(4, 5, 'python '))

#obs: se a gente informar um numero errado de paramentro ou argumentos, teremos TypeError

#print(soma(2, 3, 4)) # typeError - passando argumentos a mais
#print(soma(4)) # typeError - passando argumentos a menos
"""
# nomeando parametro


def nome_completo(nome, sobrenome):
    return f'seu nome completo é {nome}{sobrenome}'

print(nome_completo('wesley ', 'freire'))

# a diferença entre parametros e argumentos

#parametros são variaveis declaradas na definição de uma função;
#argumentos são dados passados durante a execução de uma função;

# a ordem dos parametros importa