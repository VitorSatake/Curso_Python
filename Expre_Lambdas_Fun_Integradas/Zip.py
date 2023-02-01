"""
Zip

zip() -> cria um iteravel (Zip Object) que agrega elementos de cada um dos iteraveis passados como entrada em pares.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, set ou dicionario 

print(list(zip1))
#print(tuple(zip1))
#print(set(zip1)) # gera nao ordenado
#print(dict(zip1)) # nesse caso nao consegue com o 'abc', pois dict é uma chave um valor

# OBS : Após executar uma vez, some da memoria, ou seja, precisa executar novamente pra passar para tupla, set e dict
# O zip() utiliza como parametro o menor tamanho em iteravel, isso significa se estiver trabalhando com iteraveis de 
# tamanhos diferentes ira parar quando os elementos do menor iteravel acabar.

# Podemos utilizar diferentes iteraveis com zp()

tupla = 1,2,3,4,5
lista = [6,7,8,9,10]
dict = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dict.values())
print(list(zt))

# Lista de tuplas

dados = [(0,1), (2,3), (4,5)]

print(list(zip(*dados))) # * desempacota os dados


"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

print(list(zip(alunos, prova1, prova2)))

final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)} # pega a maior nota de cada um

print(final)

# Podemos utilizar o map para fazer isso

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))