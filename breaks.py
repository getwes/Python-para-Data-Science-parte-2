"""
saindo de loops com break

funciona da mesma forma que nas linguagens c ou java.

ultilizamos o break para sair de loops de maneira projetada.
"""

# exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('sai do loop')