"""
Reduce

OBS : A partir do python 3+ a função reduce() nao é mais uma função integrada (built-in). Agora temos que
importar e utilizar esta função a partir do modulo 'functools'

Guido van Rossum: Utilize a função reduce() se voce realmente precisa dela. Em todo caso, 99% das vezes
um loop for é mais legivel.

Para entender o reduce()

# Imagine que voce tem uma coleção de dados:

dados = [a1, a2, a3 ... an]

# E voce tem uma função que recebe dois parametros

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parametros: a função e o iteravel

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:

    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função pasando o resultado do passo 1 + o terceiro elemento e guarda o resultado

    Isso é repetido até o final !!!
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = (resn, an)

Ou seja, em cada passo ela aplica a função passando como o primeiro argumento o resultado da aplicação anterior.
No final, reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como :

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""

# Como funciona na pratica ?

# Vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2,3,4,5,7,11,13,17,19,23,29]

# Para utilizar o reduce() nos precisamos de uma funcao que recebe dois parametros
multi = lambda x, y: x * y

res = reduce(multi, dados)

print(res)

# Utilizando um loop normal

res = 1

for n in dados:
    res = res * n

print(res)