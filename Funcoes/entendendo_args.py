""""
Entendendo o *args

- O *args é um parametro, como outro qualquer. Isso significa que voce podera chamar
de qualquer coisa, desde que comece com asteristico.

Exemplo:

*xis

Mas por convenção, utilizamos o *args para defini-lo

Mas oque é o *args ?

O parametro *args utilizado em uma função, coloca os valores extras informados como entrada
em uma tupla. Entao desde ja, lembre que tiplas sao imutaveis.

# Exemplo

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

# print(soma_todos_numeros(4, 6)) TypeError, menos argumentos
# print(soma_todos_numeros(4, 6, 9, 5)) TypeError, mais argumentos

# Entendendo o *args

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(2, 3, 4, 5))

# Mesmo exemplo de outra forma, com menos linha de codigo

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(2, 3, 4, 5))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    return 'Eu nao sei quem voce é !'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
"""

def soma_todos_numeros(*args):
    #print(args) # imprime a lista como um unico elemento
    return sum(args)

numeros = [1, 2, 3, 4]

num1, num2, num3, num4 = numeros

# Desempacotador

print(soma_todos_numeros(*numeros)) # avisando o Python que é uma coleção de dados,
#dessa forma com o * sabe que precisa desempacotar para fazer a operação

#print(soma_todos_numeros(numeros)) # TypeError, nao consegue imprimir listas