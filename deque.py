"""
modulo collections - deque

podemos dizer que o dequer é uma lista de alta perfomace.


"""
#import

from collections import deque

#criando deques

deq = deque('wesley')

print(deq)

#adcionando elementos no deque

deq.append('f') # adciciona no final

print(deq)

deq.appendleft('s') # adciona no começo

print(deq)

#remover elementos

print(deq.pop()) # remove e retorna o ultimo elemento

print(deq)