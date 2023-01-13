"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parametro seja opcional;

def exponencial(numero, potencia=2): # coloca o 2 como padrao para a potencia
    return numero ** potencia

print(exponencial(3)) # nao precisa do segundo parametro, é opcional, pois esta como padrao 2
print(exponencial(3, 5)) # quando informa a potencia como argumento, utiliza o valor informado

# OBS : Se o usuario passar somente um argumento, este sera atribuido ao parametro numero, e sera calculado
# o quadrado desse numero
# Se o usuario passar 2 argumentos, o primeiro sera para numero e o segundo para potencia

# Se quiser que os dois valores sejam opcionais, é só atribuir um valor para o numero, igual a potencia

# Em funções Python, os parametros com valores padrao DEVEM sempre estar ao final da declaração

# Erro

def teste(num=2, potencia): 
    return num ** potencia

# Correto

def teste(potencia, num=2): 
    return num ** potencia
"""

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que voce fosse o instrutor'
    return f'Ola {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
