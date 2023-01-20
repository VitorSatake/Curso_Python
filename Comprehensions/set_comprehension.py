"""
Set Comprehension

"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro Exemplo

numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio : Faça uma alteração na estrutura acima, para gerar um dicionario, ao invés de set

numeros = {x:x ** 2 for x in range(10)}
print(numeros)

# Para finalizar

letras = {letra for letra in "Geek University"} # nao tem ordenação nem repetição
print(letras)