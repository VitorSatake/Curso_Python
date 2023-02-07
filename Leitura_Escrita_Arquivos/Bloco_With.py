"""
O bloco With

Passos para se trabalhar com arquivos:

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados sao fechados apos
o bloco with.

arquivo = open('texto.txt')
"""

# O bloco with - forma Pythonica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed) # verifica dentro do with se esta aberto, da false pois ainda esta aberto

print(arquivo.closed) # verifica fora do with se esta aberto, da true pois fechou apos a execução do bloco

