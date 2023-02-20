""" 
mapas -> conhechecidos como dicionarios

dicionarios em python são representados por chavess {}
"""
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
#interar sobre dicionarios
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])