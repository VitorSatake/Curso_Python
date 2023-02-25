"""
POO - Métodos

- Métodos (funçoes) -> Representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar 
no seu sistema.

Em Python dividimos os metodos, em dois grupos, Métodos de Instaancia e Métodos de Classe.

# Metodos de Instancia

# O metodo dunder init __init__ é um metodo especial chamado de construtor, e sua funçao éconstruir o objeto 
a partir da classe.

# OBS : Todo elemento em python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

# OBS : Os metodos dunder em python sao chamados de metodos magicos.

ATENÇAO : Por mais que possamos criar nossas proprias funções utilizando dunder, nao é aconselhado.
Python possui varios metodos com esta forma de nomenclatura, e pode ser que mudemos o comportamento dessas funções 
magicas internas da linguagem, entao evite ao maximo, de preferencia nunca o faça.

# OBS : Metodos sao escritos em letras minusculas, se o nome for compsto, o nome tera as palavras separadas
por underline.
"""

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador +1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return (f'{self.__nome} {self.__sobrenome}.')
    
    def retorna_senha(self):
        return self.__senha



p1 = Produto('Playstation', 'Video Game', 2300)

print(p1.desconto(10))

user1 = Usuario('Renato', 'Augusto', 'teste@gmail', 1234)

print(user1.nome_completo())
print(user1.retorna_senha())

user2 = Usuario('Fabio', 'Albuquerque', 'teste2@gmail.com', 4567)

print(user2.nome_completo())
print(user2.retorna_senha())

