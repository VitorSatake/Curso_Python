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
"""




