"""
**kwargs
poderiamos chamar este parametro de **xis, mas por conveção chamamos de **kwargs

este é so mais um parametro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que ultilizamos parametros nomeados, e trasforma esses
parametros extras em um dicionario.
"""

#exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'a cor favorita de {pessoa} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')