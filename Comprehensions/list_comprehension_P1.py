"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de
outro iteravel.

# Sintaxe da List Comprehension

[ dado for dado in iteravel ]

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


Para entender melhor oque esta acontecendo, devemos dividir a expressao em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10



res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor*valor

res = [funcao(numero) for numero in numeros]
print(res)

# List Comprehension versos Loop

# Loop

numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero*2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehension

print([numero*2 for numero in numeros])
numeros_dobrados2 = [numero*2 for numero in numeros] # ou atribuindo em uma variavel

print(numeros_dobrados2)
"""
# Outros Exemplos

# 1

nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.upper() for amigo in amigos[0]]) # caixa alta por indice da lista

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper()) # trocaa a primeira letra de cada palavra, por maiuscula
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# 3

print([numero*3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]]) # transforma os numeros em string