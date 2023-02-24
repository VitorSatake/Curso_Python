"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto, ou seja , pelos atributos nós conseguimos
representar computacionalmente os estados de um objeto.

Em python dividimos os atributos em 3 grupos :
    - Atributos de instancia;
    - Atributos de classe;
    - Atributos de dinamicos;

# Atributo de instancia: Sao atributos declarados dentro do metodo construtor.

# OBS: Metodo construtor : é um metodo especial utilizado para a construção do objeto.

# OBS : Em python, por convenção, ficou estabelecido que todo atributo de uma classe é publico.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da propria classe onde está declarado,
utiliza-se __ duplo underscore no inicio de seu nome.

Isso é conhecido tambem como Name Mangling.

"""
# Classes com atributo de instancia publico

class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos publicos e atributos privados:

class Acesso:
    def __init__(self, email, senha):
        self.email = email 
        self.__senha = senha



# OBS : Lembre-se que isso é apenas uma convenção, ou seja , a linguagem python nao vai impedir
# que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '12345')

print(user.email)
#print(user.__senha) # AttributeError
print(user._Acesso__senha) # Temos acesso, mas nao deveriamos fazer esse acesso.