""" 
mapas -> conhechecidos como dicionarios

dicionarios em python são representados por chavess {}
"""
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
#interar sobre dicionarios
for chave in receita:
    print(chave) # aqui estamos imprimindo apenas as chaves

for chave in receita:
    print(receita[chave])  # nesse estamos imprimendo  apenas os valores 100 , 120 , 300