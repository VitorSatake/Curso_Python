"""
**Kwargs

Poderiamos chamar este parametro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parametro, mas diferente do *args que coloca os valores extras em uma tupla , 
o **kwargs exige que utilizemos parametros nomeados, e transforma esses parametros extras em um dicionario.

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}') # title deixa letra maiuscula

cores_favoritas(a=1, b=2, c=3, marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parametros *args e **kwargs nao sao obrigatorios

cores_favoritas()
cores_favoritas(geek='navy')

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs ['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Nao tenho certeza quem você é !' 

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções, podemos ter (NESTA ORDEM): # caos necessite declarar todos esses parametros

- Parametros Obrigatorios;
- *args;
- Parametros default (nao obrigatorios);
- **kwargs;

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Nao', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entendendo por que é importante manter a ordem dos parametros na declaração

# Função com a ordem corretaa de parametros

#def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parametros

def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

a =1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes)) # desempacotar o **kwargs

"""
def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
#soma_multiplos_numeros(1, 2, 3)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS : Os nomes da chave em um dicionario, devem ser os mesmos dos parametros da função

#dicionario = dict(d=1, e=2, f=3)  # TypeError

#soma_multiplos_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='Geek')

soma_multiplos_numeros(**dicionario, lang='Python')