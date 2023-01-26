"""
Any e All

all() -> retorna True se todos os elementos do iteravel sao verdadeiros, ou ainda se o iteravel esta vazio

# Exemplo all()

print(all([0, 1, 2, 3, 4])) # Todos os numeros sao verdadeiros ? False, pq 0 é False
print(all([1, 2, 3, 4])) # Agora sem o 0, True
print(all([])) # Vazio, retorna True
print(all(['Geek'])) # Retorna True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano']
print(all([nome[0] == 'C' for nome in nomes])) # True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Daniel']
print(all([nome[0] == 'C' for nome in nomes])) # False

# OBS : Um iteravel vazio convertido em boolean , é False , mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([numero for numero in [4, 2, 10, 6, 8] if numero % 2 == 0])) # Retorna True, mesmo se 1, pq gera uma lista vazia

any() -> Retrona True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio, retorna False
"""
print(any([0,1,2,3,4])) # retorna true, se qualquer um for true

print(any([0,False,{},(),[]])) # tudo False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Vanessa']

print(any([nome[0] == 'C'for nome in nomes])) # True pq precisa apenas ser True

print(any(num for num in [4,2,10,6,8] if num % 2 == 0)) # True