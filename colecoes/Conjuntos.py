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

#Conjuntos nao aceitam valores duplicados, por isso 6 elementos, e gera uma ordenação própria
conjunto = {99, 3, 23, 47, 11, 5, 23, 99}
print(f'Set : {conjunto} com {len(conjunto)} elementos.') # nao repete valores

#Listas aceitam valores duplicados, por isso 8 elementos , gera a ordenação que está feita
lista = [99, 3, 23, 47, 11, 5, 23, 99]
print(f'Lista : {lista} com {len(lista)} elementos.')

#Tuplas aceitam valores duplicados, por isso 8 elementos , gera a ordenação que está feita
tupla = (99, 3, 23, 47, 11, 5, 23, 99)
print(f'Tupla : {tupla} com {len(tupla)} elementos.')

#Dicionarios nao aceitam valores v(chaves) duplicados, por isso 6 elementos , gera a ordenação que está feita
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

# Adicionando elementos em um conjunto

s = {1, 2, 3}
print(s)
s.add(4)
s.add(4) # Duplicidade nao gera erro, simplesmente é ignorado e nao é adicionado
print(s)

# Remover elemnetos em um conjunto

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3) # nao é indice! informamos o valor a ser excluido. Nenhum valor é retornado
print(s)

# OBS : caso o valor nao seja encontrado, sera gerado o erro KeyError

# Forma 2

s.discard(2)
print(s)

# OBS : caso o valor nao seja encontrado, nao sera gerado nenhum erro # Remover elemnetos em um conjunto

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3) # nao é indice! informamos o valor a ser excluido. Nenhum valor é retornado
print(s)

# OBS : caso o valor nao seja encontrado, sera gerado o erro KeyError

# Forma 2

s.discard(2)
print(s)

# OBS : caso o valor nao seja encontrado, nao sera gerado nenhum erro 

# Copiando um conjunto para outro

# Forma 1 - Deep Copy

novo = s.copy()  
print(novo)

novo.add(4) # adiciona só no novo, nao no original (s)
print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s 

novo.add(4) # adiciona em ambos, no novo e no original

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Métodos matematicos de conjuntos

# Imagine que temos dois conjuntos: um contendo estudantesdo curso Python e um
# contendo estudantes do curso Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}

estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python, tambem estudam Java

# Precisamos gerar um conjunto com nomes de estudantes unico

# Forma 1 - Utilizando Union

unicos1 = estudantes_python.union(estudantes_java) # gera sequencia de forma aleatoria (mais recomendado)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java # gera sequencia de forma aleatoria

print(unicos2)

# Gerar um conjunto de estudantes que estao em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java) # gera de forma aleatoria
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java # gera de forma aleatoria
print(ambos2)

# Gerar um conjunto de estudantes que nao estao no outro curso

so_python = estudantes_python.difference(estudantes_java) # gera de forma aleatoria
print(so_python)

so_java = estudantes_java.difference(estudantes_python) # gera de forma aleatoria
print(so_java)
"""

s = {1, 2, 3, 4, 5, 6}
print(s)

# Soma*, Valor Maximo*, Valor minimo*, Tamanho

# * Se os valores forem todos inteiros ou todos reais

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

