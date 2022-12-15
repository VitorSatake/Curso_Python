"""
Loop For

Loop = estrutura de repetição

for item in interável:
    //execução do loop

Utilizamos loop para iterar sobre sequencias ou sobre valores iteraveis

Exemplo de iteraveis: string, lista, range
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # temos que transformar em uma lista

#Exemplo de for 1 (iterando em uma string)

for letra in nome: 
    print(letra)

#Exemplo de for 2 (iterando em uma lista)

for num in lista:
    print(num)

"""Exemplo de for 3 (iterando em um range) range(valor_inicial, valor_final)
Obs: o valor final não é inclusive
1
2
3
4
5
6
7
8
9
10 - NÃO
"""
for num2 in numeros:
    print(num2)    

for i, v in enumerate(nome): #Enumerate indice, valor ((0, 'G'), (1, 'e'), (2, 'e') ...)
    print(v)

for _, v in enumerate(nome): # _ descarta o indice, se nao for necessario .. pode ser para qualquer valor
    print(v)

for valor in enumerate(nome): # faz o for printando indice e valor, util para pegar somente o indice que precisar
    print(valor)
    print(valor[0]) # imprime somente os indices
    print(valor[1]) # imprime somente os valores ( as letras nesse caso )
print(nome[5]) # imprimindo pelo indice desejado

qtd = int(input('Quantas vezes esse loop deve rodar ? '))

for n in range(1, qtd + 1): # + 1 paraa pegar até onde o usuario solicitou
    print(f'Imprimindo {n}')

qtd2 = int(input('Quantas vezes esse loop deve rodar ? '))
soma = 0

for n2 in range(1, qtd2 + 1): # + 1 paraa pegar até onde o usuario solicitou
    num3 = int(input(f'Informe o {n2}/{qtd2} valor : ')) # vai pedindo valor a valor 
    soma = soma + num3 # faz as somas dos valores pedidos 
print(f'Imprimindo {soma}')


for letra3 in nome: 
    print(letra3, end='') # imprime tudo na mesma linha

# segurando CTRL + clicando no print(exemplo), gera a documentação do print

print(nome * 3) # da pra multiplicar strings

# Tabela de emojis Unicode : https://apps.timwhitlock.info/emoji/tables/unicode

# Original : U+1F60D
#Modificado : U0001F60D , no + por 3 zeros

emoji = '\U0001F60D' # tem que usar a barra invertida para passar

for num in range(1, 11):
    print(f'{emoji * num}')

for _ in range(3): # faz 3 vezes o for de baixo
    for num in range(1, 11):
        print(f'{emoji * num}')    

