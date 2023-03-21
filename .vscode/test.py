"""
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1
"""
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['w', 'e', 's', 'l', 'e', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Wesley da Silva Freire')


lista1.extend(lista2)
print(lista1)
"""
# iniciar uma procura de itens
#  no super mercado para compor uma cesta basica.
"""
type([])

listamercado = ['arroz', 'feijao', 'oleo', 'sal', 'cafe', 'milho', 'biscoito', ]


if 'arroz' in listamercado:
    print("temos arroz")
else:
    print("nao temos arroz")

if 'chocolate' in listamercado:
    print("temos chocolate")
else:
    print(f"nao temos chocolate")

    # teste

    br = 'brasil'
pa = 'paris'
ru = 'rusia'

pais = input('digite o nome do seu pais: ')
if pais == br:
    print('seu pais é brasi')
elif pais == pa:
    print('seu pais é paris')
elif pais == ru:
    print('seu pais é paris')
else:
    print(' não encontrei seu pais')

    
    produtos = ["ABC123", "acd012", " ABS111", "AbB222"]

#texto = "abd012"
#texto = texto.upper() # upper() serve para trasformar as letras minusculas em maiusculas
#texto = texto.strip() # strip() serve para remover espaços do começo e do fim
#print(texto)

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto

#texto = " abd012 "
#texto = tratar_texto(texto)
#print(texto)

for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto)

dados = produtos.copy()
print(dados)


def diz_oi():
    return 'oi'

def diz_tudo_bem():
    return 'tudo bem ?'

print(f'retorno de {diz_oi()}  {diz_tudo_bem()}')

print(35 % 2)
"""

