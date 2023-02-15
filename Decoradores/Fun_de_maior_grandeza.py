"""
Funções de Maior Grandeza - Higher Order Functions - HOF

Oque isso significa ?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como
resultado, ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar
variaveis do tipo de funções nos nossos programas.

OBS : Na sessão de funções, utilizamos isso.

Em Python, as funções sao cidadaos de primeira classe, First Class Citizen


# Exemplos - Definindo as funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções

print(calcular(3, 5, somar))
print(calcular(3, 5, diminuir))
print(calcular(3, 5, multiplicar))
print(calcular(3, 5, dividir))

# Nested Functions - Funções Aninhadas

#Em python podemos tambem ter funções dentro de funções, que sao conhecidas por Nested Functions, ou tambem
#Inner Functions ( Funções Internas)

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de voce '))
    return humor() + pessoa


# Testando 


print(cumprimento('Angelina'))
print(cumprimento('Viviane'))


# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahaha', 'kkkkkkkk', 'hihihihihi'))
    return rir

# Testando

rindo = faz_me_rir()
print(rindo())   


"""

# Inner Functions - Funções Internas / Nested Functions , podem acessar o escopo de funções mais externas

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'kkkkkkkk', 'hihihihihi'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando 

rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())