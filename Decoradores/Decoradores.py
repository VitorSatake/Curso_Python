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


# Decoradores com Syntax Sugar (Açucar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um bom dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# Testando

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir!')


dormir()
"""

# Web Site
"""
 | -----------------------------------------
 |  Home   | Serviços  | Produtos  | Adm   |

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/serviços

http://www.suaempresa.com.br/produtos

http://www.suaempresa.com.br/adm

# Nao é codigo funcional (que funcione) apenas exemplo

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/login')


def home(request):
    return 'Pode acessar home'

def servicos(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login # decorator para checar o login para acesso a adm
def adm(request):
    return 'Pode acessar adm'
"""

# OBS : Nao confunda Decorator com Decorator Function

"""
# Decorator Function

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/login')

# Decorator 

@checa_login

"""