"""
Decoradores ( Decorators )

O que sao decorators ?

- Decorators sao funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators sao exemplos de Higher Order Functions;
- Decorators tem uma sintaxe propria, usando "@" (Syntact Sugar / Açucae Sintatico)

/ ----------------------------------- /
/        Function Decorator           /
--------------------------------------

---------------------------------------
/ / ----------------------------------- / /
/ /         Funcão Decorada               / /
/ /------------------------------------/ /
/ --------------------------------------

# Decorators como funções (Sintaxe nao recomendada / Sem açucar simpatico)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voce')
        funcao()
        print('Tenha um otimo dia')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) a Geek Universtity')

# Testando 1

#saudacao()

teste = seja_educado(saudacao)

teste()

# Testando 2


def raiva():
    print('EU TE ODEIO')

raiva_educada = seja_educado(raiva)

raiva_educada()
"""

