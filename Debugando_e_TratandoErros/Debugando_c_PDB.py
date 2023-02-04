"""
debuggando com PDB

PDB -> Python Debbuger

Bug -> inseto

# OBS : A utilização do print para debugar codigo é uma pratica ruim.
def dividir(a, b):
    print(f'a: {a}, b: {b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:  # Forma semi-generica
        return f'Ocorreu um problema: {err}!'

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando o PDB - Python Debugger

#Exemplo com o PyCharm

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:  # Forma semi-generica
        return f'Ocorreu um problema: {err}!'

print(dividir(4, 7))

# Exemplo com PDB - Python Debugger - Exemplo 1

# Para utilizar o PDB, precisamos* importar a biblioteca PDB e entao utilizar a função set_trace()

# Comandos basicos do PDB
# l (kistar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)


import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programaação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo com PDB - Python Debugger - Exemplo 2

# Para utilizar o PDB, precisamos* importar a biblioteca PDB e entao utilizar a função set_trace()

# Comandos basicos do PDB
# l (kistar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)


#import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace() # fazendo o import direto na linha do codigo
nome_completo = nome + ' ' + sobrenome
curso = 'Programaação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Porque utilizar  este formato ?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso, ao inves de colocarmos o import do pdb no inicio do arquivo,
# nos colocamos somente onde debuggar, e ao finalizar ja fazemos a remoção.

# Exemplo com PDB - Python Debugger - Exemplo 3

# Para utilizar o PDB, precisamos* importar a biblioteca PDB e entao utilizar a função set_trace()

# * A partir do python 3.7 nao é mais necessario importar a biblioteca pdb, pois o comando de debug
# foi incormporado como função built-in (integrada) chamada breakpoint()

# Comandos basicos do PDB
# l (kistar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)


#import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint() # utilizando o breakpoint inves de importar o pdb
nome_completo = nome + ' ' + sobrenome
curso = 'Programaação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

# OBS : Cuidado com conflitos entre nomes de variaveis e os comandos do PDB

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c # para resolver o conflito usar o 'p' para imprimir variavel

print(soma(1, 3, 5, 7))

# Como os nomes das variaves sao os mesmos dos comandos pdb, devemos utilizar o comando p
# para imprimir as variaveis. Ou seja: p nome_da_vaiavel

# Nada de colocar nomes nao representativos em variaveis, sempre optar por nomes significativos.