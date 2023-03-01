"""
POO - Herança Multipla

Herança Multipla nada mais é que a possibilidade de uma classe herdar de multiplas classes.
Fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas

OBS : A herança multiplapode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;


# Exemplo 1 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class Multiderivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass
    

OBS: Nao importa se a derivação é direta ou indireta, a classe que realizar a herança, herdara todos 
os atributos e metodos das super classes.
"""

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}.'
    

class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar.'
    

class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.' 
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra.'
    


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


    
# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) # ???? Eu sou Tux da terra. Method Resolution Order (MRO)
# Se alterar a ordem de herança de Pinguim para (Aquatico, Terrestre) imprime Eu sou Tux do mar, pois altera
# a ordem de execução da herança.

# Objeto é instancia de ...

print(f'Tux é instancia de pinguim? {isinstance(tux, Pinguim)}') # True
print(f'Tux é instancia de Aquatico? {isinstance(tux, Aquatico)}') # True
print(f'Tux é instancia de Terrestre? {isinstance(tux, Terrestre)}') # True
print(f'Tux é instancia de Object? {isinstance(tux, object)}') # True
print(f'Tux é instancia de Animal? {isinstance(tux, Animal)}') # True