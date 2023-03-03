"""
definindo funçoes

- funçoes são pequenas partes codigos que realizam tarefas especificas;
- pode ou não receber entrada de dados e retornar uma saida de dados;
-muito uteis para executar procedimentos similares por repetidas vezes;

obs: se você escrever uma função que realiza varias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificadas.

ja ultilizamos varias funções desde que iniciamos este curso:
print()
len ()
max ()
min ()
count()
e muitas outras;
"""
# exemplo de ultilização de funçoes:

#cores = ['verde', 'amrelo', 'azul', 'branco']

#ultilizando a função integrada (built-in) do python print()

#print(cores)

#curso = 'programação em python: essencial'

#print(curso)

#cores.append('preto')

#print(cores)

#curso.append('mais dados...')  # AttributeError: 'str' object has no attribute 'append'  
#print(curso)

#cores.clear()
#print(cores)

#print(help(print))

#dry - don´t repeat yourself -não repita voce mesmo; nãoo repita seu codigo.

# mas então como definir funçoes??

#"""
#em python, a forma geral definir uma função é:

#def nome_da_função(parametro_de_entrada):
    #bloco_da_função

#onde:

#nome_da_função -> sempre com letras minuscolas, e se for nome composto, separado por underline (snake case);
#parametros_de_entrada -> opicionais, onde tendo mais de um, cada um separado por vigula, podendo ser opcionais ou não;
#bloco_da_função -> tambem chamado de corpo da função ou implementação, é onde o processamento da função acotece.
#neste bloco, pode ter ou não retorno da função.

#obs: veja que para definir uma função, utilizamos a palavra reservada 'def' informado ao python que
#estamos definindo uma função. tambem abrimos o bloco de codigo com o ja conhecido dois pontos:
#utilizado em python para definir blocos.
#"""

# definido a primera função
#definição
def diz_oi():
    print('oi')

#obs:

# 1 - veja que, dentro das nossas funções podemos utilizar outras funções;
# 2 - veja que nosa função so executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer oi;
# 3 - veja que esta função não recebe nem um parametro de entrada;
# 4 - veja que esta função não retorna nada;

#utilizando funçoes

#chamada de execução
diz_oi()

#ATENÇÃO NUNCA ESQUEÇA DE UTILIZAR O PARÊNTESES AO EXECUTAR UMA FUNÇÃO.

#exemplo:
#errado
#diz_oi

#certo
#diz_oi()

# exemplo 2
def cantar_parabens():
    print('parabens para você')
    print('nesta data querida')
    print('muitas felicidades')
    print('viva o aniversariante!')

#for n in range(5):
    #cantar_parabens()
    
# em python podemos inclusive criar variaveis do tipo de uma função e executar esta função atraves da variavel

canta = cantar_parabens

canta()