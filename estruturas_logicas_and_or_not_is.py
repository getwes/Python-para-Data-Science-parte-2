"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

operadores unários:
- not , is
operadores binários:
- and, or

Regras de funcionamento
para o 'and', ambos os valores precisam ser True
para o 'or', um ou outro valor precisa ser True
para o 'not', o valor do boolean é invertido, ou seja, se for true, vira false, se for false vira true
"""

ativo = True
logado = True

if ativo and logado:
    print('bem-vindo usuáriio!')
else:
    print('você precisa ativar sua conta. por favor, cheque seu e-mail')