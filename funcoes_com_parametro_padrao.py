"""
funçoes com parametro padrão (defalt paramters)

- funções onde a passagem de parametros seja opcional;

# exemplo de função onde a passagem de parametro seja opcional
print('wesley freire')

print()

#exemplo de função onde a passagem de parametros seja obrigatoria
def quadrado(numero):
    return numero ** 2
    
print(quadrado(3))
print(quadrado()) # typeError

def exponencial(numero=4, potencia=2): # quando passo esse =2 faz com oque o parametro seja ou não opicional
    return numero ** potencia

print(exponencial(2, 3)) # 2 * 2 * 2 = 8
print(exponencial(3, 2)) # 3 * 3 = 9

print(exponencial(3)) #por padrão eleve ao quadrado
print(exponencial(3, 5)) # eleve á potencia informada pelo usuario
#obs
# se o usuario passar somente 1 argumento, este sera atribuido ao parametro numero, e sera calculado o quadrado deste numero;
# se o usuario passar 2 argumentos, o primero sera atribuido ao parametro numero e o segundo ao parametro potencia. então
#sera calculada a esta potencia.

print(exponencial())

#obs: em função python, os parametros com valor default (padrão) DEVEM sempre esta ao final da declaração.

#erro
def teste(num=2, potencia): #caso queira concluir essa operação so inverter num e potencia
    return num ** potencia

print(teste(6))
   
# outros exemplos

def soma(num1, num2):
    return num1 + num2

print(soma(1, 3))
print(soma(4))#typeError
print(soma())#typeError


def soma(num1=5, num2=3):
    return num1 + num2

print(soma(1, 3))
print(soma(4))
print(soma())

#exemplo mais complexo

def mostra_informacao(nome='wesley', instrutor=False):
    if nome == 'wesley' and instrutor:
        return f'bem vindo instrutor {nome}'
    elif nome == 'wesley':
        return 'pensei que era o instrutor'
    return f'ola {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('ozzy'))

# por que ultilizar parametros com valor default?

- nos permite ser mais flexiveis na função;
- evita erros com parametros incorretos;
- nos permite trabalhar com exemplos mais legiveis de codigos;

#quais tipos de dados podemos ultilizar como valores default para parametro?

-qualquer tipo de dado:
- numeros, strings, floats, booleanos, listas, tuplas, dicionarios, funçoes e etc;

# exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1 , num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 3, subtracao))

# escopo - evitar problemas e confusões

#variaveis globais
#variaveis locais

instrutor = 'wesley' # varaivel global

def diz_oi():
    instrutor = 'python' # variavel local
    return f'oi {instrutor}'

print(diz_oi())

#obs: se tivermos uma variavel local com o mesmo nome de uma varaivel global, a local tera preferencia.

def diz_oi():
    prof = 'geek' #varaivel local
    return f'ola {prof}'

print(diz_oi())

print(prof) # nameError

# ATENÇÃO com variveis globais (se puder evitar, evite!)

total = 0

def incremeto():
    total = total + 1 #UnboundLocalError( a variavel local esta sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incremeto())

# resolvendo

total = 0

def incremeto():
    global total # avisando que queremos utilizar a variavel global
    total = total + 1 
    return total

print(incremeto())
print(incremeto())
print(incremeto())
"""
# podemos ter funções que são decladas dentro de funções, e tambem tem uma forma especial de escopo de variavel

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())