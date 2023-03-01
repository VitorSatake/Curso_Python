"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Quando a gente reimplementa um metodo presenta na classe pai em uma classe filha,
estamos realizando uma sobrescrita de metodo (Overriding)

O overriding é a melhor representação para o polimorfismo.
"""

class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse metodo.')
    
    def comer(self):
        print(f'{self.__nome} está comendo ...')



class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala au au!')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau!')


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self): # se nao implementar: raise NotImplementedError('A classe filha precisa implementar esse metodo.')
        print(f'{self._Animal__nome} fala algo ...!')


# Testando

felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()