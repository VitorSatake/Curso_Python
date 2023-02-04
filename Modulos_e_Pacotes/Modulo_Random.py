"""
Modulo Random e oque sao modulos?

- Em Python, modulos nada mais sao que outros arquivos Python.

Modulo Random -> possui varias funções para geração de numeros pseudo-aleatorios (pode ser que haja repetição).

# OBS : Existem duas formas de se utilizar um modulo ou função deste

# Forma 1 - Importando todo o modulo (Nao recomendado)

import random

# random() -> gera um numero real pseudo-aleatorio entre 0 e 1

# OBS: Ao realizar o import de todo o modulo, todas as funções, atributos, classes e propriedades que estiverem dentro
# do modulo ficarão disponiveis (Ficarão em memoria). Caso voce saiba quais funções vpce precisa utilizar deste modulo
# entao esta nao seria a forma ideal de utilização, nós veremos uma forma melhor na forma 2.

#print(dir(random))
#print(help(random.random))

print(random.random())

# OBS : Veja que para utilizar a função random() do pacote random, nos colocamos o nome do pacote e o nome da função
# separados por ponto.

# OBS : Nao confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é 
# apenas uma função dentro do modulo random.

# Forma 2 - Importando uma função especifica do modulo (Forma recomendada)

from random import random

# No import acima estamos falando: Do modulo random, importe a função random

for i in range(10):
    print(random())


# uniform() -> Gerar um numero real pseudo-aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # O 7 nao é incluido


# randint() -> Gera valores inteiros pseudo-aleatorios entre os valores estabelecidos

from random import randint

# Gerados de apostas para a mega-sena


for i in range(6):
    print(randint(1, 61), end=', ') # substitui para nao pular uma linha, mas separando por virgula (começa em 1 até 60)

# choice() -> mostra um valor aleatorio entre um iteravel

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

# choice() -> mostra um valor aleatorio entre um iteravel

from random import choice

print(choice('Geek University')) # escolhe uma letra no iteravel passado
"""

from random import shuffle

# shuffle() -> tem a função de embaralhar dados

cartas = ['k', 'q', 'j', 'a', '2', '3', '4']

print(cartas)

shuffle(cartas) # embaralha

print(cartas[0]) # devolve uma carta
print(cartas.pop()) # retira e devolve a ultima carta

