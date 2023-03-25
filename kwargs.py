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

# nas nossas funçoes podemos ter (NESTA ORDEM):

-parametros obrigatorios;
- *args;
-parametros default (não obrigatorios);
--**kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(18, 'felicity' , 4, 5, 3, solteiro=True)
minha_funcao(34, 'felipe', eu='não', voce='vai')
minha_funcao(19, 'carla', 9, 4, 3, java=False, python=True)

#resultado

julia tem 8 anos
()
casado
{}
felicity tem 18 anos
(4, 5, 3)
solteiro
{}
felipe tem 34 anos
()
casado
{'eu': 'n�o', 'voce': 'vai'}
carla tem 19 anos
(9, 4, 3)
casado
{'java': False, 'python': True}

"""
# entenda por quer é importante manter a ordem dos parametrosd na declaração

#função com a ordem correta de parametros
def mostra_info(a, b, *args, instrutor='geek', **kwargs): #os parametros feito de forma errada pode ocorrer uma quebra no resultado
    return [a, b, args, instrutor, kwargs]

"""
a = 1
b = 2
args = (3,)
instrutor ='geek'
kwargs = {'sobrenome': 'university', 'cargo': 'instrutor'}
"""
print(mostra_info(1, 2, 3, sobrenome='university', cargo='instrutor'))