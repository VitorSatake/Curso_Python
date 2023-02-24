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
        self.email = email # publico
        self.__senha = senha # privado

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)



# OBS : Lembre-se que isso é apenas uma convenção, ou seja , a linguagem python nao vai impedir
# que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '12345')

print(user.email)
#print(user.__senha) # AttributeError
print(user._Acesso__senha) # Temos acesso, mas nao deveriamos fazer esse acesso. (Name Mangling)

user.mostra_senha() # função criada dentro da classe para mostrar a senha

# O que significa atributos de instancia ?

# Significa que ao criarmos instancias/objetos de uma classe, todas as instancias terao esses atributos.

user1 = Acesso('user1@gmail.com', '1234')
user2 = Acesso('user2@gmail.com', '5678')
user3 = Acesso('user3@gmail.com', '0000')

user1.mostra_senha()
user2.mostra_senha()
user3.mostra_senha()

user3.mostra_email()



# Atributos de Classe

p1 = Produto('PlayStation', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

# Atributos de classe sao atributos, que sao declarados diretamente na classe, ou seja, fora do construtor
# Geralmente ja inicializamos um valor, e este valor é compartilhado entre todas as instancias da classe.
# Ou seja, inves de cada instancia da classe ter seus proprios valores como é o caso dos atributos de instancia, 
# com os atributos de classe todas as instancias terao o mesmo valor para este atributo

# Refatorar a classe Produto

class Produto:

    #Atributo de classe
    imposto = 1.05 # 0.05 % de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p3 = Produto('PlayStation', 'Video Game', 2300)
p4 = Produto('Xbox S', 'Video Game', 4500)

print(p3.imposto) # mesmo valor pra os dois
print(p4.imposto) # mesmo valor pra os dois

print(p3.valor) # valor calculado sobre cada valor, acesso possivel mas incorreto de um atributo de classe
print(p4.valor) # valor calculado sobre cada valor, acesso possivel mas incorreto de um atributo de classe

# OBS : Nao precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # diretamente atraves da classe, faz acesso a instancia de classe, acesso correto

print(p3.id) # contador inicia em 0 e soma 1 para iniciar os ids dos objetos
print(p4.id) # contador atualiza para aumentar os ids dos objetos


# Atributos Dinamicos -> Um atributo de instancia que pode ser criado em tempo de execução

# OBS : O atributo dinamico, será exclusivo da instancia que o criou

p5 = Produto('PlayStation', 'Video Game', 2300)
p6 = Produto('Xbox S', 'Video Game', 4500)

# Criando um atributo dinamico em tempo de execução

p5.peso = '5kg' # note que na classe produto nao existe o atributo peso
#p6.peso = '15kg'

print(f'Produto: {p5.nome}, descriçao: {p5.descricao}, valor: {p5.valor}, peso: {p5.peso}.')
#print(f'Produto: {p6.nome}, descriçao: {p6.descricao}, valor: {p6.valor}, peso: {p6.peso}.') # erro, pois
# nao existe o atributo peso

# Deletando atributos

print(p5.__dict__) # __dict__ propriedades do objeto
print(p6.__dict__)

# Deletando

del p5.peso # atributo dinamico
del p5.valor # atributo de instancia, tambem deleta
del p5.descricao # atributo de instancia, tambem deleta

print(p5.__dict__) # sem o peso