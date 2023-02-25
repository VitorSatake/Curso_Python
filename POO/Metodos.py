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

#OBS : Metodos de classe em python, sao conhecidos como metodos estaticos em outras linguagens.
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


from passlib.hash import pbkdf2_sha256 as cryp # biblioteca para criar criptografia 

"""
class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return (f'{self.__nome} {self.__sobrenome}.')
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False



#p1 = Produto('Playstation', 'Video Game', 2300)

#print(p1.desconto(10))

user1 = Usuario('Renato', 'Augusto', 'teste@gmail', '1234')

#print(user1.nome_completo())
#print(user1.retorna_senha())

user2 = Usuario('Fabio', 'Albuquerque', 'teste2@gmail.com', '4567')

#print(user2.nome_completo())
#print(user2.retorna_senha())


nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere.')
    exit(1)

print('Usuario criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido.')
    print(f'Senha User Criptografada: {user1._Usuario__senha}')  # Acesso errado (Isso é salvo no banco de dados)
else:
    print('Acesso negado!')

#print(f'Senha User Criptografada: {user1._Usuario__senha}')  # Acesso errado


# Metodos de Classe

# Refatorando classe Usuario


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe {cls}')
        print(f'Temos {cls.contador} usuários no sistema')


    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return (f'{self.__nome} {self.__sobrenome}.')
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    

user8 = Usuario('Angelina', 'Jolie', 'ang@gmail.com', '123456')

Usuario.conta_usuarios() # Forma correta
user8.conta_usuarios() # possivel , mas incorreta

# Usa Metodo de instancia quando precisa de acesso a atributos de instancia
# Usa Metodo de classe quando nao precisa fazer acesso a atributos de instancia



# Refatorando Usuario com metodo privado

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe {cls}')
        print(f'Temos {cls.contador} usuários no sistema')


    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return (f'{self.__nome} {self.__sobrenome}.')
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    def __gera_usuario(self): # metodo privado, inicia com __
        return self.__email.split('@')[0] # separa pelo @ e retorna o indice 0, retorna só o nome
    

#user = Usuario('Angelina', 'Jolie', 'ang@gmail.com', '123456')
"""
# Metodo Estatico

# Refatorando com metodo estatico

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe {cls}')
        print(f'Temos {cls.contador} usuários no sistema')

    @staticmethod # metodo estatico
    def definicao():
        return 'UXR344'


    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return (f'{self.__nome} {self.__sobrenome}.')
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    def __gera_usuario(self): # metodo privado, inicia com __
        return self.__email.split('@')[0] # separa pelo @ e retorna o indice 0, retorna só o nome


print(Usuario.contador)
print(Usuario.definicao())

user = Usuario('Angelina', 'Jolie', 'ang@gmail.com', '123456')

print(user.contador)
print(user.definicao())