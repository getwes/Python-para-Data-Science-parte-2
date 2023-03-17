"""
entendendo *args
- o *args é um parametro, como outro qualquer. isso significa que voce podera
chamar de qualquer coisa, desde que começe com asterisco.

exemplo

*xis

mas por convenção, utilizamos *args para defini-lo

mas oque é o *args??

o parametro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. então dede ja lembre-se que tuplas são imutaveis.

# exemplos

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6, ))

print(soma_todos_numeros(4, 6, 9, 5))

#entendendo o args

#def soma_todos_numeros(*args):
    #total = 0
   # for numero in args:
         # total = total + numero
    #return total

def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('angelina', 'jolie'))
print(soma_todos_numeros('angelina', 'jolie',1))
print(soma_todos_numeros('angelina', 'jolie', 2, 3))
print(soma_todos_numeros('angelina', 'jolie' ,2, 3, 4))
print(soma_todos_numeros('angelina', 'jolie', 3, 4, 5, 6))

print(soma_todos_numeros('angelina', 'jolie', 23.4, 12.5))

# outro emplo de utilização do *args

def verifica_info(*args):
    if 'wesley' in args and 'freire' in args:
        return 'bem-vindo wesley'
    return 'eu não tenho certeza quem voce é'

print(verifica_info())
print(verifica_info(1, True, 'freire', 'wesley'))
print(verifica_info(1 , 'freire', 3.145))
"""

def soma_todos_numeros(*args):
    return sum(args)


#print(soma_todos_numeros())
#print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# desempacotador 

# o * serve como desempacotador pois estou utilizando uma lista

print(soma_todos_numeros(*numeros))

#obs: o asterisco serve para que informemos oa python que estamos
#passando como argumento uma coleção de dados. desta forma, ele saberá
#que precisará antes desempacotar este dados.