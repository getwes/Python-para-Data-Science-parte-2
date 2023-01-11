"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

operadores unários: # depende apenas de um valor
- not 
operadores binários:
- and, or, binario is

Regras de funcionamento
para o 'and', ambos os valores precisam ser True
para o 'or', um ou outro valor precisa ser True
para o 'not', o valor do boolean é invertido, ou seja, se for true, vira false, se for false vira true
para o 'is' o valor é comparado com um segundo. # usa-se para comparação
"""

ativo = False
logado = True
""""
if ativo and logado:
    print('bem-vindo usuáriio!')
else:
    print('você precisa ativar sua conta. por favor, cheque seu e-mail')
"""

if  ativo is logado:
    print('bem-vindo usuario')
    
else:
    print('voce precisa ativar sua conta. por favor, cheque seu e-mail')
#ativo é falso?
print( ativo is True)