"""
POO - Propriedades (Properties)


Em linguagens como java, usa get e set.

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def tranferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite


conta1 = Conta('Bruno', 3000, 5000)
conta2 = Conta('Pedro', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é {soma}')
"""

# Refatorando com propriedade

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def tranferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
  
    
conta1 = Conta('Bruno', 3000, 5000)
conta2 = Conta('Pedro', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')