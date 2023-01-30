"""
Sorted

OBS : Nao confunda, apesar do nome, com a função sort() que ja estudamos em listas. O sort()
só funciona em listas.

# sort()
lista = [4, 7, 3, 1, 2]
lista.sort() # sort() , ordena lista apenas
print(lista)

Podemis utilizar o sorted() com qualquer iteravel.

Como o proprio nome diz, sorted() serve para ordenar elementos.

OBS: O sorted() sempre retorna uma lista com os elemntos do iteravel ordenados

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros)) # Ordenar do menor para o maior
print(numeros)

# Adicionando paraametros ao sorted()

numeros = [6, 1, 8, 2]

print(numeros)

print(tuple(sorted(numeros))) # normalmente sorted retorna uma lista, mas aqui passmos para tupla

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor, ordena e inverte a lista

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [],}
]

print(usuarios)

# Ordenando pelo username, ordem alfabetica

print(sorted(usuarios, key= lambda usuario: usuario["username"])) # ordena pela primeira letra do username

print(sorted(usuarios, key= lambda usuario: usuario["username"], reverse=True)) # ordena pela primeira letra do username, na forma reversa

# Ordenando pelo numero de tweets, do menor pro maior

print(sorted(usuarios, key= lambda usuario: len(usuario["tweets"])))
"""

# Ultimo exemplo


musicas = [
    {"titulo": "Thunder", "tocou": 3},
    {"titulo": "Dead Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old", "tocou": 32}
]

print(musicas)

# Ordena da menos tocada para a mais tocada

print(sorted(musicas, key=lambda musica: musica["tocou"]))

# Ordena da mais tocada para a menos tocada

print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))

