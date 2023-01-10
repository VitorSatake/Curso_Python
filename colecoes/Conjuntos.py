"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a Teoria dos Conjuntos
da Matemática.

- Aqui no Python os conjuntos sao chamados de Sets.

Dito isto, da mesma forma que na matematica:
-Sets (conjuntos) nao possuem valores duplicados;
-Sets (conjuntos) nao possuem valores ordenados;
-Elementos nao sao acessados via indice, ou seja, conjuntos nao sao indexados

Conjuntos sao bons para se utilizar quando precisamos armazenar elementos, mas nao nos importamos 
com a ordenação deles. Quando nao precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) sao referenciados em Python com chaves {}

Diferença entre conjuntos (set) e mapas (dicionarios) em Python :

    - Um dicionario tem chave / valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # repare que temos valores repetidos

print(s) # nao imprime os valores repetidos, e nao gera erro
print(type(s))

# OBS : ao criar um conjunto caso seja adicionado um valor ja existente, o mesmo sera ignorado
# sem gerar erros e nao fara parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}

print(s)
print(type(s))

# Podemos verificar se determinado elemento esta contido no conujunto

if 3 in s:
    print('Tem o 3')
else:
    print('Nao tem o 3')

# Importante lembrar que além de nao termos valores duplicados, nao temos ordem

#Conjuntos nao aceitam valores duplicados, por isso 6 elementos
set = {99, 3, 23, 47, 11, 5, 23, 99}
print(f'Set : {set} com {len(set)} elementos.') # nao repete valores

#Listas aceitam valores duplicados, por isso 8 elementos
lista = [99, 3, 23, 47, 11, 5, 23, 99]
print(f'Lista : {lista} com {len(lista)} elementos.')

#Tuplas aceitam valores duplicados, por isso 8 elementos
tupla = (99, 3, 23, 47, 11, 5, 23, 99)
print(f'Tupla : {tupla} com {len(tupla)} elementos.')

#Dicionarios nao aceitam valores v(chaves) duplicados, por isso 6 elementos
dicionario = {}.fromkeys([99, 3, 23, 47, 11, 5, 23, 99], 'dict')
print(f'Dicionario : {dicionario} com {len(dicionario)} elementos.') # nao repete chaves

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44, }
print(s)
print(type(s))

# Podemos iterar em um Set normalmente

for valor in s:
    print(valor)

# Usos interessantes com Sets

# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu, 
# e os visitantes informaram manualmente a cidade de onde vieram.

# Nos adicionamos cada cidade em uma lista Python, ja que em umalista podemos adicionar novos elementos e 
# ter repetição

cidades = ['Belo Horizonte', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Sao Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora preciasamos saber quantas cidades distintas , ou seja, unicas , temos

# O que voce faria ? Faria um loop na lista ?

# Podemos utilizar o Set para isso

print(len(set(cidades)))
print(set(cidades)) # elimina as repetidas
"""

