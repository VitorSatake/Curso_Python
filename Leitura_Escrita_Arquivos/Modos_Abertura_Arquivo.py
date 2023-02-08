"""
Modos de abertura de arquivo

r -> Abre para leitura - padrao.
w -> Abre para escrita - sobrescreve caso o arquivo ja exista.
x -> Abre para escrita somente se o arquivo nao existir. Caso o arquivo exista gera : FileExistsError.
a -> Abre para escrita adicionando o conteudo ao final do arquivo.
+ -> Abre para o mode de atualização: Leitura e Escrita.

# OBS : abrindo no modo 'a' -> append, se o arquivo nao existir será criado. Caso exista,
o conteudo será adicionado SEMPRE no final do arquivo. Com o modo 'a' nao controlamos o cursor.

https://docs.python.org/3/library/functions.html#open

# Exemplo 'x'
# Tente abrir, caso FileExistsError, print
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo.\n')
except FileExistsError:
    print('Arquivo ja existe.')


# Exemplo 'a'

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""

with open('frutas.txt', 'r+') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
