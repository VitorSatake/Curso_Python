"""
Seek e Cursors

seek() -> é utilizada para movimentar o cursor pelo arquivo (seek -> procurar)

arquivo = open('texto.txt')
print(arquivo.read())

# seek() -> a função seek() é utilizada para movimentação do cursor pelo arquivo,
# ela recebe um parametro que indica onde queremos colocar o cursor

# Movimentando o cursor pelo arquivo com a função seek()

arquivo.seek(0) # seek(0) coloca o cursor novamente no começo para permitir imprimir novamente abaixo

print(arquivo.read()) # nova impressao

arquivo.seek(22) # seek(0) coloca o cursor novamente a partir do caractere 22 para permitir imprimir novamente abaixo

print(arquivo.read()) # nova impressao

arquivo = open('texto.txt')

# readline() -> função que lê o arquivo linha a linha

#print(arquivo.readline()) # imprime linha 1
#print(arquivo.readline()) # imprime linha 2
#print(arquivo.readline()) # imprime linha 3

ret = arquivo.readline()
print(type(ret))
print(ret)
print(ret.split(' ')) # gera lista separada por espaço

arquivo = open('texto.txt')

# readlines() -> gera uma lista com cada linha sendo um objeto da lista

linhas = arquivo.readlines()

print(len(linhas)) # mostra quantas linhas com conteudo tem o arquivo

# OBS : quando abrimos um arquivo com a função open() é criada uma conexao entre o arquivo no disco
do sistema operacional (computador) e o nosso programa. Essa conexao é chamada de streaming. Ao finalizar os trabalhos
com o arquivom, devemos fechar essa conexao, para isso utilizamos a função close().

Passos para se trabalhar com um arquivo:

1- Abrir o arquivo;

2- Trabalhar o arquivo;

3 - Fechar o arquivo;

# 1- Abrir o arquivo;
arquivo = open('texto.txt')

# 2- Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed) # verifica se o arquivo está aberto ou fechado, retorna true ou false, nesse caso false pois esta aberto

# 3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed) # retorna true apos fechar o arquivo

# print(arquivo.read()) # tentar ler um arquivo ja fechado  ValueError: I/O operation on closed file.

# OBS : se tentarmos manipular um arquivo ja fechado, teremos um ValueError.
"""

arquivo = open('texto.txt')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo.

print(arquivo.read(50)) # limita aos primeiros 50 caracteres