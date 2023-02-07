"""
Leitura de Arquivos

Para ler o conteudo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parametro de entrada,
que neste caso é o coaminho para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que 
trabalhamos então.

Para saber mais:
https://docs.python.org/3/library/functions.html#open

# OBS : Por padrao a função open() abre o arquivo para leitura, este arquivo deve existir, ou entao teremos
o erro FileNotFoundError.

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -> modo de leitura. r -> read() -> ler.
"""

# Exemplo

arquivo = open('texto.txt')

#print(arquivo)

#print(type(arquivo))

# Para ler o conteudo de um arquivo, apos sua abertura, devemos utilizar a função read()

ret = arquivo.read()

print(type(ret))

print(ret)

#print(arquivo.read())

# OBS : O Python utiliza um recurso para trabalhar com arquivos chamado curso. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

#print(arquivo.read())

# OBS : A função read() lê todo o conteudo do arquivo.