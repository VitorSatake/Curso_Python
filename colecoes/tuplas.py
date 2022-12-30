"""
Tuplas (tuple)

Tuplas sao bastanta parecidas com listas, existem daus diferentes basicas:

1 - as tuplas sao representados por parenteses ()

2 - As tuplas sao imutaveis, isso signfica que ao criar uma tupla ela nao muda,
toda operação em uma tupla gera uma nova tupla.

# Cuidado 1: As tuplas sao representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6 # tambem tupla
print(tupla2)
print(type(tupla2))

# Cuidado 2 : Tuplas com um elemento

tupla3 = (1) # isso nao é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (1,) # isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 1, # isso é uma tupla
print(tupla5)
print(type(tupla5))

# CONCLUSAO : Podemos concluir que tuplas sao definidas pela virgula, e nao pelo uso do ()

(4) -> Nao é tupla
(4,) -> É tupla
4, -> É tupla

# Podemos gerar uma tupla dinamicamente com range (inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python Essencial')

escola, curso = tupla # primeiro valor para escola, segundo valor para curso

print(escola)
print(curso)

# OBS : gera erro (ValueError), se colocarmos um numero diferente de elementos para desempacotar.

# Metodos para adição e remoção de elementos nas tuplas nao existem, dado o fato das tuplas serem imutaveis

# Soma*, vamor maximo*, valor minimo* e tamanho
# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2 # usa a mesma variavel para concatenar, sem precisar criar outra
print(tupla1)

# Verificar se determinado elemento esta contido na tupla

tupla1 = (1, 2, 3)
print(3 in tupla1)
print(33 in tupla1)

# Iterando sobre uma tupla
tupla1 = (1, 2, 3)
for n in  tupla1:
    print(n)

for indice, valor in enumerate(tupla1): # imprime com indice e valor
    print(indice,valor)


# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))

escola = tuple('Geek University') # converte uma string em uma tupla
print(escola)
print(escola.count('e')) # conta quantos 'e' tem em Geek university

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que nao precisar modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'todos os meses')

# O acesso a elementos de uma tupla também é semelhante de uma lista

print(meses[2]) # acesso pelo indice 2

# Iterar com While

i = 0

while i < len(meses):
    print(meses[i])
    i = i +1

meses = ('Janeiro', 'Fevereiro', 'Março', 'todos os meses')

# Verificaos em qual indice um elemento esta em uma tupla

print(meses.index('Março')) # mostra o indice de março

# OBS : Caso o elemento nao exista, sera gerado erro

meses = ('Janeiro', 'Fevereiro', 'Março', 'todos os meses')

# Slicing

# tupla[inicio:fim:passo]

print(meses[0:]) # imprime do primeiro ao ultimo

print(meses[0:2]) # imprime o primeiro e o segundo

# Porque utilizar tuplas ?

# Tuplas sao mais rapidas que listas
# tuplas deixam seu codigo mais seguro -> imutabilidade

"""

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla nao tem o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla) # nao altera a tupla original