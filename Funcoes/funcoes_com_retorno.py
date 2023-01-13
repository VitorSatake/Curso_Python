"""
Funções com retorno

OBS : Em Python quando uma função nao retorna nenhum valor, o retorno é None

OBS : Funções Python que retornam valores devem retornar estes valores com a palavra reservada RETURN

OBS : Nao precisamos necessariamente criar uma vaariavel para receber o retorno de uma função.
Podemos passar a execução da função para outras funções.

# Exemplo função

def quadrado_de_7():
    print(7 * 7)

quadrado_de_7()

# Vamos refatorar (reescrever) esta função para qque ela retorne o valor

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7() # Criamos uma variavle para receber o retorno da função
print(f'Retorno {ret}')

print(f'Retorno {quadrado_de_7()}') # Passando a função direto

# Refatorando a primeira função

def diz_oi():
    return 'Oi!'

print(diz_oi()) # como só retorna, tem que colocar no print

alguem = 'Pedro'

print(diz_oi() + alguem) # com o return te da mais flexibilidade de usar

OBS: Sobre a palavra reservada return:

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter em uma função, diferentes returns;
3 - Podemos em uma função retornar qualquer tipo de dado, até mesmo multiplos valores;

# Exemplo 1 - 1 - Ela finaliza a função, ou seja, ela sai da execução da função;

def diz_oi():
    return 'Oi!'
    print('Estou sendo executado apos o retorno') # nao executa pois o return finaliza a função

print(diz_oi())

# Exemplo 2 - 2 - Podemos ter em uma função, diferentes returns;

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'

print(nova_funcao())

# Exemplo 3 - 3 - Podemos em uma função retornar qualquer tipo de dado, até mesmo multiplos valores;

def outra_funcao():
    return 2, 3, 4, 5

num1 , num2, num3, num4 = outra_funcao() # desempacotando
print(num1 , num2, num3, num4) # imprime de forma separada

print(outra_funcao()) # imprime uma tupla

# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um numero pseudo-randomico (pode ser que haja repetição) entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

def joga_moeda():
    # Gera um numero pseudo-randomico (pode ser que haja repetição) entre 0 e 1
    if random() > 0.5: # outra forma colocando direto o random, sem criar uma variavel e atribuir
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
"""

# Erros comuns na utilização do retornon que nao sao erros, mas sim codificação desnecessaria

def eh_impar():
    numero = 5
    if numero %2 != 0:
        return True
    #else: nao precisa colocar o else com duas opçoes só
    return False

print(eh_impar())



