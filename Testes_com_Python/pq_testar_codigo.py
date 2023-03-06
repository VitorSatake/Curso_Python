"""
Porque testa nosso codigo ?

Testes automatizados !

---------------------------------------
|                                      |
|       frontend e backend             |  Aplicação Web
---------------------------------------
|        testes automatizados          |
---------------------------------------

Porque testar nosso codigo ?

    - Reduzir bugs (problemas) no codigo existente;
    - Testes garantem que novos recursos da sua aplicação nao quebrem (alterem) recursos antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos;
    - Testes garantem que a refatoração que costumamos fazer, nao tragam novos bugs;

TDD - Test Driven Development (Desenvolvimento guiado por testes)

Com TDD é utlizado estagios de desenvolvimento:
    - Voce escreve seu teste primeiro;
    - Entao voce escreve seu codigo minimo suficiente para fazer o teste passar(ou seja, executar com sucesso);
    - Entao refatora o codigo para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe , o recurso é considerado completo;


Estes estagios de desenvolvimento do TDD sao quase como um mantra que os desenvolvedores seguem, conhecido como:
    - Red;
    - Green;
    - Refactor;
"""

class Gato:
    def __init__(self, nome):
        self.__nome = nome


    @property
    def nome(self):
        return self.__nome
    
    def miar(self):
        print(f'{self.__nome} esta miando ...')



felix = Gato('Felix')

felix.miar()

print(felix.nome)