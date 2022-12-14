"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa
2 - Variáveis locais
    - Variáveis globais são reconhecidas apenas no bloco onde foi declarada, ou seja, seu escopo 
    está limitado ao seu bloco aonde foi declarado

nome_da_variavel = valor_da_variavel

|                     | <- espaço 

Python é uma linguagem de tipagem dinamica. Significa que ao declarar uma variavel não precisa
colocar o tipo dela. Esse tipo é inferido ao atribuir o valor a mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

#Exemplo de variavel global

numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

#Exemplo de variavel global

num = 42

def soma():
    if num > 10:
        novo = num + 10 # novo variavel local
        print(novo)

soma()

# nao aceita print(novo) pq foi declarado local dentro da função




