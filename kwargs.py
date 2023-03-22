"""
**kwargs
poderiamos chamar este parametro de **xis, mas por conveção chamamos de **kwargs

este é so mais um parametro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que ultilizamos parametros nomeados, e trasforma esses
parametros extras em um dicionario.

#exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'a cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# obs: os parametros *args e ** kwargs não são obrigatorios
cores_favoritas()

cores_favoritas(geek='navy')

# exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'wesley' in kwargs and kwargs['wesley'] == 'python':
        return 'voce recebeu um cumprimento pythonico'
    elif 'wesley' in kwargs:
        return f"{kwargs['wesley']} wesley"
    return ' não tenho certezxa de quem voce é'

print(cumprimento_especial())
print(cumprimento_especial(wesley='python'))
print(cumprimento_especial(wesley='oi'))
print(cumprimento_especial(geek='especial'))
"""

