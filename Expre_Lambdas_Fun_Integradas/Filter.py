"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleçao.

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores)) # media

print(media)

for n in valores: # for para achar os numeros maiores que a media
    if n > media:
        print(n)

# Biblioteca para trabalhar com dados estatisticos

import statistics

# Dados coletados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a media dos dados utilizando a função mean()

media = statistics.mean(dados) # faz a media
print(f'\nMedia: {media}\n')

# OBS : Assim como a função map(), a filter recebe 2 parametros, sendo uma função e um iteravel

res = filter(lambda x: x > media, dados) # funçao que retorna os numeros maiores que a media
print(type(res)) # retorna filter object
print(list(res))

print(f'Novamente {list(res)}') # retorna vazia, pq ja utilizou uma vez, que nem o map

# OBS : Assim como na função map(), após serem utilizados os dados de filter(), eles sao excluidos da memoria 

# Filtrando os dados vazios

# Exemplo 1

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises) # None, filtra (elimina) os dados vazios

print(list(res))

# Exemplo 2

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(lambda pais: len(pais) > 0, paises) # função lambda que retorna o valor de pais maior que 0, eliminando os vazios

print(list(res))

# Exemplo 3

res = filter(lambda pais: pais != '', paises)

print(list(res))

# A diferença entre map() e filter() é :

# map() -> Recebe dois parametros, uma função e um iteravel e retorna um objeto mapeando a função para cada elemento do iteravel

# filter() -> Recebe dois parametros, uma função e um iteravel e retorna um objeto filtrando apenas os elemento de acordo com a função

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Filtrar os usuarios que estao inativos no Twitter

# Forma 1

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# Forma 2

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios)) # not nega, lista vazia transformada em boolena é False
print(inativos)

"""
# Como combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
