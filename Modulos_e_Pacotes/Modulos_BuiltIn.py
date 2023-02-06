"""
Trabalhando com Modulos Builtin (modulos integrados que ja vem instalados no Python)

 |Python|Modulos builtin|


# Utilizando alias (apelidos), para modulos/funções

import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um modulo utilizando o *

from random import *

print(random())

# Importando todo o modulo

import random

print(random.random())

# Utilizando alias (apelidos), para modulos/funções - Uma funçao

from random import randint as rdi

print(rdi(5, 89))

# Utilizando alias (apelidos), para modulos/funções - Duas funçoes

from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())

"""
# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo modulo 
from random import (
    random,
    randint,
    shuffle, 
    choice
)

print(random())

print(randint(3, 10))

lista = ['Geek', 'University']
shuffle(lista)
print(lista)

print(choice('Geek University'))