"""
Generator Expression

Em aulas anteriores nós estudamos:
    - list comprehension
    - dictionary comprehension
    - set comprehension

Nao vimos:
    - Tuple comprehension .. porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Vanessa']
print(any([nome[0] == 'C'for nome in nomes]))

# Poderiamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Vanessa']
print(any(nome[0] == 'C'for nome in nomes))

# List Comprehension

res = [nome[0] == 'C'for nome in nomes]
print(type(res)) 
print(res) # cria a lista em memória

# Generator

res = (nome[0] == 'C'for nome in nomes)
print(type(res)) 
print(res) # cria o objeto, nao ocupa ainda a memoria

# Generator ocupa menos recurso em memória, e mais performance

# Qual a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parametro
from sys import getsizeof

# Mostra quantos bytes a string Geek esta ocupando em memória. Quanto maior, maior espaço ocupa
print(getsizeof('Geek'))

print(getsizeof('Geek University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(943543534534))

print(getsizeof(True))
"""
from sys import getsizeof

# Gerando uma lista de numeros com list comprehension

list_compre = getsizeof([x * 10 for x in range(1000)])

# Gerando um conjunto de numeros com set comprehension

set_compre = getsizeof({x * 10 for x in range(1000)})

# Gerando um dicionario de numeros com dictionary comprehension

dict_compre = getsizeof(({x: x * 10 for x in range(1000)}))

# Gerando uma lista de numeros com generators

gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memoria: \n')
print(f'List Comprehension: {list_compre} bytes')
print(f'Set Comprehension: {set_compre} bytes')
print(f'Dictionary Comprehension: {dict_compre} bytes')
print(f'Generator Expression: {gen} bytes')


# Eu posso iterar no Generator Expression ? Sim !!!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for numero in gen:
    print(numero)