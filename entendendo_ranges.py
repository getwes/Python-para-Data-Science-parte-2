"""
Ranges

- precisamos conhecer o loop for para usar os ranges.
precisamos conhcer o range para trabalhar melhor com o loops for

ranges são utilizadas para gerar sequencias numerica, 
não de forma aleatroira, mas sim de maneira especificada.

forma gerais:

range(valor_de_parada)

obs: valor_de_parada não  inclusive (inicio padrão 0, e passo de 1 em 1)

#exemplo forma 1

for num in range(11):
    print(num)

# exemplo forma 2
#range(valor_de_inicio, valor_de_parada)
#obs: valor_de_paradaa não inclui (inicio especificodo pelo usuario, e passo de 1 em 1)
for num in range(1, 11):
    print(num)

#exemplo forma 3

#range(valor_de_inicio, valor_de_parada)
#obs: valor_de_paradaa não inclui (inicio especificodo pelo usuario, e passo especificado pelo usuario )

for num in range(1, 10, 2): # começã com o numero 1 vai ate o numero 10 e vai pulando de 2 em 2 numeros
    print(num)
"""
#forma 4 (inversa)

#range(valor_de_inicio, valor_de_parada, passo)

#obs: valor_de_paradaa não inclui (inicio especificodo pelo usuario, e passo especificado pelo usuario )

# exemplo forma 4
for num in range(10, 0, -1 ):
    print(num)