"""
Teste de Velocidade com Expressoes Geradoras

# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()

print(ge1) # Generator
print(next(ge1))
print(next(ge1))
print(next(ge1))

# Generator Expression

ge2 = (num for num in range(1, 10))

print(ge2) # Generation Expression

print(next(ge2))
print(next(ge2))
print(next(ge2))
"""

# Realizando Teste de Velocidade
import time

# Generaator Expression / 5.55492639541626 segundos

gen_inicio = time.time()
print(sum(num for num in range(0, 100000000)))
#print(type(num for num in range(1, 10)))
gen_tempo = time.time() - gen_inicio

# Lista Comprehension / 8.49571442604065 segundos

list_inicio = time.time()
print(sum([num for num in range(0, 100000000)]))
list_tempo = time.time() - list_inicio


print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')