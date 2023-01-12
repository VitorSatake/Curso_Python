"""
Modulo Collections -> Ordered Dict

# Em um dicionario a ordem de inserção dos elementos nao é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

Ordered Dict -> é um dicionario que nos garante a ordem de inserção dos elementos

# Fazendo o import

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')
"""
from collections import OrderedDict

# Entendendo a diferença entre Dict e Orderd Dict

# Dict

dict1 = {'a': 1, 'b':2}
dict2 = {'b':2, 'a': 1}

print(dict1 == dict2) # True or False ? True, ja que a ordem dos elementos nao importa para o dicionario

# Ordered Dict

dict3 = OrderedDict({'a': 1, 'b':2})
dict4 = OrderedDict({'b':2, 'a': 1})

print(dict3 == dict4) # True or False ?  False, pq a ordem faz diferença