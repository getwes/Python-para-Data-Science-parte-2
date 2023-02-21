""" 
mapas -> conhechecidos como dicionarios

dicionarios em python são representados por chavess {}

#interar sobre dicionarios
for chave in receita:
    print(chave) # aqui estamos imprimindo apenas as chaves

for chave in receita:
    print(receita[chave])  # nesse estamos imprimendo  apenas os valores 100 , 120 , 300

for chave in receita:
    print(f' em {chave} recebi R$ {receita[chave]}')

#acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

#acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)
"""
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

#desempacotamento de dicionarios
print(receita.items())
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')