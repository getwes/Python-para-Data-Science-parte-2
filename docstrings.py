"""
documentando funçõs com docstrings

obs: podemos ter acesso a documentação de uma função em python
ultilizando a propriedade especial__doc__

podemos ainda fazer acesso a documentação com a função help()
"""
def diz_oi():
    """ uma função simples que retorna a string oi"""
    return 'oi'

print(diz_oi())

def exponencial(numero, potencia=2):
    """
    podemos fazer documentação dentro  de funções
    """
    return numero ** potencia

