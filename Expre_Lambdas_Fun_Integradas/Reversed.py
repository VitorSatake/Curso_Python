"""
Reversed

OBS: Naao confunda com a função reverse() que estudamos nas listas

A função reverse(), funciona apenas em listas.

Ja a função reversed() funciona com qualquer iteravel.

Sua função é inverter o iteravel.

A função reversed() retorna um iteravel chamado List Reversed Iterator
"""

# Exemplo

lista = [1,2,3,4,5]

res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemnto retornado para uma lista , tupla ou conjunto

# Lista

print(list(reversed(lista)))

# Tupla

print(tuple(reversed(lista)))

# Set (Conjunto), em conjunto nao definimos a ordem dos elementos

print(set(reversed(lista))) # nao faz o reversed(), pq set nao define ordem

# Podemos iterar sobre o reversed()

for letra in reversed('Geek University'):
    print(letra, end=' ')

print('\n')

# Podemos fazer o mesmo sem o uso do for 

print(''.join(list(reversed('Geek University'))))

# Ja vimos como fazer isso mais facil com o slice de strings

print('Geek University'[::-1])

# Podemos tambem utilizar o reversed() para fazer um loop for reverso

for n in reversed(range(0, 10)):
    print(n)

# Apesar que tambem ja vimos como fazer isso utilizando o proprio range() inverso

for n in range(9, -1, -1):
    print(n)