"""
Erros mais comuns

# ATENÇAO !!!
É importante prestar atenção e aprender a ler as saidas de erro geradas pela execução do nosso codigo.


OS erros mais comuns:

1 - SyntaxError -> ocorre quando o python encontra algum erro de sintaxe, ou seja, voce escreveu algo que o python
nao reconhece como parte da linguagem.

# Exemplos SyntaxError

a)

def funcao:
    print('Geek')

b)

None = 1
def = 2

2 - NameError -> ocorre quando uma variavel ou funçao nao foi definida

# Exemplos NameError

a)

print(geek)

b)

geek()

3 - TypeError -> ocorre quando uma função/operação/ação é aplicada a um tipo errado

# Exemplos TypeError

print(len(4)) # tipo int nao tem len()

print('geek' + [])

4 - IndexError -> ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um indice invalido

lista = ['geek']
print(lista[2])

5 - ValueError -> ocorre quando uma função ou operação built-in (integrada) recebe um argumento com tipo
correto mas valor inapropriado.

print(int('geek'))

6 - KeyError -> ocorre quando tentamos acessar um dicionario com uma chave que nao existe

dict = {}
print(dict['geek'])

7 - AttributeError -> ocorre quando uma variavel nao tem um atributo/função

tupla = (11, 2, 31, 4)

print(tupla.sort())

8 - IndentationError -> ocorre quando nao respeitamos a indentação do python (4 espaços)

def nova():
print('geek')

OBS : Exceptions e Errors sao sinonimos na programação.

OBS : Importante ler e prestar atenção na saida de erro.
"""





