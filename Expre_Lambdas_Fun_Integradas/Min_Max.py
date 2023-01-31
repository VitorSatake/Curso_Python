"""
Min e Max

max() -> retorna o maior valor em um iteravel ou o maior de dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129] # pode ser lista, tupla, set ... # max(dicionario.values()), para pegar o maior valor de um dicionario

print(max(lista))

# Faça um programa que receba dois valores do usuario e mostre o maior

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(f'Valor 1: {val1}, valor 2: {val2}')

print(f'Maior valor: {max(val1, val2)}')

print(max(4, 56, 129)) # com 3 valores

print(max('a', 'ab', 'abc')) # por numero de letras

print(max('a', 'b', 'c')) # por sequencia do alfabeto

print(max('Geek University')) # pega ultima letra em relação ao alfabeto

min() -> retorna o menor valor em um iteravel ou o menor de dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129] # pode ser lista, tupla, set ... # min(dicionario.values()), para pegar o menor valor de um dicionario

print(min(lista))

# Faça um programa que receba dois valores do usuario e mostre o menor

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(f'Valor 1: {val1}, valor 2: {val2}')

print(f'Menor valor: {min(val1, val2)}')

print(min(4, 56, 129)) # com 3 valores

print(min('a', 'ab', 'abc')) # por numero de letras

print(min('a', 'b', 'c')) # por sequencia do alfabeto

print(min('Geek University')) # pega primeira letra em relação ao alfabeto, nesse caso o menor é o espaço

# Outros exemplos

nomes = ['Arya', 'Sanson', 'Dora', 'Tim', 'Olivander']

print(max(nomes)) # Tim, pela letra do alfabeto que inicia

print(min(nomes)) # Arya, pela letra do alfabeto que inicia

print(max(nomes, key=lambda nome: len(nome))) # Olivander, pelo numero de letras (lambda: para cada nome da lista de nomes, ordene pelo tamanho de nome)

print(min(nomes, key=lambda nome: len(nome))) # Tim, pelo numero de letras
"""
musicas = [
    {"titulo": "Thunder", "tocou": 3},
    {"titulo": "Dead Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO  !  Imprima somente o titulo da musica mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO ! Como encontrar a musica mais tocada e a menos tocada sem usar max(), min() e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])


min = 9999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])