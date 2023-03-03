"""
Conhecendo Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

# OBS: O modulo Pickle nao é seguro contra dados maliciosos, e dessa forma, nao é recomendado trabalhar 
com arquivos Pickle vindo de outras pessoas que voce nao conheça ou de fontes desconhecidas.

# Fazendo a escrita em arquivos Pickle

felix = Gato('Felix')
pluto = Cachorro('Pluto')


with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""

import pickle

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f'{self.nome} está comendo ...')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando ...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo ...')



# Fazendo a leitura de dados em arquivos Pickle


with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')



