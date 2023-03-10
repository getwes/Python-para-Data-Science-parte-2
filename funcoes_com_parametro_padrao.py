"""
funçoes com parametro padrão (defalt paramters)

- funções onde a passagem de parametros seja opcional;

# exemplo de função onde a passagem de parametro seja opcional
print('wesley freire')

print()

#exemplo de função onde a passagem de parametros seja obrigatoria
def quadrado(numero):
    return numero ** 2
    
print(quadrado(3))
print(quadrado()) # typeError
"""
def exponencial(numero, potencia):
    return numero ** potencia

print(exponencial(2, 3)) # 2 * 2 * 2