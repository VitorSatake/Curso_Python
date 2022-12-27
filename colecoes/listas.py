"""
Listas

Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem 
DINAMICOS e de podermos colocar QUALQUER tipo de dado.

Dinamico: nao possuem tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos,
enquanto tiver memória disponível.

Qaulquer: as listas nao possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

As listas em python sao representadas por colchetes: [] ;

"""

print(type([]))

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27] # lista de inteiros

lista2 = ['G', 'e', 'e', 'k'] # lista de string

lista3 = [] # lista vazia

lista4 = list(range(11)) # cria uma lista de dados de 0-10

print(lista4)

lista5 = list('Geek University') # gera uma lista da string, item por item

print(lista5)

# Podemos facilmente checar se determinado valor esta contido na lista
num = 18
if num in lista4:
    print(f"Encontrei o numero {num}!")
else:
    print(f"Nao encontrei o numero {num}!")


letra = 'e'
if 'e' in lista5:
    print(f"Encontrei a letra {letra}!")
else:
    print(f"Nao encontrei a letra{letra}!")

# Podemos facilmente ordenar uma lista
lista1.sort() # ordena a lista
print(lista1)

lista5.sort() # ordena tambem string
print(lista5)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista

print(lista1.count(1)) # conta o numero de vezes que aparece o 1, nesse caso
print(lista5.count('e')) # conta o numero de vezes que aparece o 'e', nesse caso

# Adicionar elementos em listas
# Obs: para adicionar valores em lista utilizamos a função append()
# Com append nos só conseguimos adicionar um elemento por vez

print(lista1)
lista1.append(42)
print(lista1) # após adicionar o 42
# erro : lista1.append(42, 23 ,34), tentar adicionar mais de um elemento

lista1.append([3, 6, 5, 32, 56]) # cria uma nova lista para adicionar mais elementos
print(lista1)

if [3, 6, 5, 32, 56] in lista1: # if para procurar a lista dentro da lista
    print("Encontrei a lista!")
else:
    print("Nao encontrei a lista!")

lista1.extend([123, 345, 567]) # faz o memso que o append, porem de forma individual, nao em formato de lista
# extend nao aceita valor unico, para isso usar append
print(lista1)

# Append e extend sempre adiciona para o final da lista

# Podemos inseris um novo elemnto informando a posição do indice
# isso nao substitui o valor inicial, apenas é deslocado para a direita
lista1.insert(2, 'Novo valor') # insert(posição no vetor, e valor desejado)
print(lista1)

# Podemos facilmente juntar duas listas

#lista6 = lista1 + lista2 cria uma nova lista 
lista1.extend(lista2) # adiciona direto na primeira lista
print(lista1)

lista1.reverse() # inverte a lista
print(lista1) # imprime de forma inversa a lista

# Copiar uma lista

lista6 = lista2.copy() # copia a lista 2 na variavel lista6
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista6)) # retorna o numero de elementos que a lista possui

# Podemos remover facilmente o ultimo elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)
lista5.pop()
print(lista5)
#print(lista5.pop())

# Podemos remover um elemnto pelo indice
# os elemntos a direita desse indice serao deslocados para a esquerda, nao fica vago a posição
# se nao houver elemnto no indice informado da erro
print(lista5)
lista5.pop(2) # () indice desejado
print(lista5)


#lista6 = list('Geek University')

# Podemos remover todos os elementos (zerar a lista)

print(lista5)
lista5.clear() # limpa a lista toda
print(lista5)

# Podemos facilmente converter uma string para uma lista
#Exemplo 1
curso = 'Programação em python'
curso = curso.split() # split separa por espaços
print(curso)
 #Exemplo 2
curso = 'Programação,em,python'
curso = curso.split(',') # split separa por espaços, passando o paramtro de sepação sendo virgula
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'python:', 'essencial']
print(lista6)
# abaixo falamos : pega a lista6, coloca espaço entre cada elemento e transforma em string
curso = ' '.join(lista6)
print(curso)

# podemos colocar qualquer tipo de dado em uma lista, inclusive misturar dados
lista7 = [1, 2.34, True, 'geek', 'd', [1,2,3], 1234]

# iterando sobre listas
# exemplo 1

for elemento in lista1:
    print(elemento)

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento # faz a soma dos elementos
print(soma)

# com while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista, ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# fazemos acesso ao s elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[2])

# fazer acesso aos elementos de forma indexada inversa, de tras pra frente
print(cores[-1])

