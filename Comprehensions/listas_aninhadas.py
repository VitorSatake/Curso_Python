"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamados de Arrays:
    - Unidimensionais ( Arrays/Vetores )
    - Multidimensionais ( Matrizes )

Em Python nós temos as Listas

numeros = [1, 2, 3, 4, 5, 6] 

# Exemplos

listas = [[1,2,3], [4,5,6], [7,8,9]] # Matriz 3 x 3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados

print(listas[0]) # por linha
print(listas[0][2]) # por linha e coluna (um elemento)
print(listas[2][1]) # por linha e coluna (um elemento)
print(listas[2][-1]) # de tras paraa frente

# Iterando com loops em uma lista aninhada

for lista in listas:
    for numero in lista:
        print(numero)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]
"""

# Outros exemplos

# Gerando um tabuleiro / matriz 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1,4)]
print(velha)

# Gerando valores iniciais 

print([['*' for i in range(1, 4)] for j in range(1, 4)])