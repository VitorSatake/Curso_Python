""""
List Comprehension

Nós podemos adiconar estruturas condicionais logicas as nossas List Comprehension
"""

# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares) # colocando na variavel
print(impares) # colocando na variavel
print([numero for numero in numeros if numero % 2 == 0]) # colocando direto no print
print([numero for numero in numeros if numero % 2 != 0]) # colocando direto no print

# Refatorar

# OBS : Qualquer numero par moeulo de 2 é 0, e 0 em python é false, not False = True
pares = [numero for numero in numeros if not numero % 2]
# OBS : Qualquer numero impar modulo de 2 é 1, e 1 em python é True
impares = [numero for numero in numeros if numero % 2]

print(pares) # colocando na variavel
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

