"""
Modulo Collectios -> Named Tuple

# Recp Tupla

tupla = (1, 2, 3)
print(tupla[1]) # acessando a tupla por indice

Named Tuple -> Sao tuplas diferenciadas, onde especificamos um nome para a mesma e tambem parametros.
"""
# Importando

from collections import namedtuple

# Precisamos definir o nome e parametros

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome') 

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Acessando os dados

# Forma 1

print(ray[0]) # idade
print(ray[1]) # raca
print(ray[2]) # nome

# Forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow')) # mostra o indice

print(ray.count('Chow-Chow')) # mostra o numero de ocorrencias