"""
Modos de abertura de arquivo

r -> Abre para leitura - padrao
w -> Abre para escrita - sobrescreve caso o arquivo ja exista
x -> Abre para escrita somente se o arquivo nao existir. Caso o arquivo exista gera : FileExistsError

https://docs.python.org/3/library/functions.html#open

"""

with open('university.txt', 'x') as arquivo:
    arquivo.write('Teste de conteudo.\n')