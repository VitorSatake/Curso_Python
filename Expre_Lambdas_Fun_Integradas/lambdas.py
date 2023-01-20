"""
Utilizando Lambdas

Conhecidas por Expressoes Lambdas ou simplesmente Lambdas, sao funções sem nome, ou seja,
funçoes anonimas.

# Função em Python

def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressao Lambda

lambda x: 3 * x + 1

# E como utilizar a expressao Lambda ? Atribui a uma variavel

calc = lambda x: 3 * x + 1

print(calc(4))

# Podemos ter expressoes lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# strip() remove espaços no inicio e no fim da string, nao tira entre nome e sobrenome

print(nome_completo('  pedro', '   silva')) # coloca em maiuscula a primeira letra, e corrige os espaços

print(nome_completo('  pedro', '   SILVA')) # corrige da mesma forma
"""

# Em funçoes Python podemos ter nenhuma ou varias entradas. Em Lambdas tambem.

amar = lambda: 'Como nao amar Python ?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ... xn: <expressao> quantos parametros quiser 

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))