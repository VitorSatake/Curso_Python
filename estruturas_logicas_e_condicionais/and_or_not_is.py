"""
Estruturas lógicas : AND, OR, NOT, IS

Operadores unários : not, is
NOT = valor do Booleano é invertido, se for True vira False e vice versa

Operadores binários : and, or
AND = ambos preciasm ser True
OR = pelo menos um precisa ser True
"""

ativo = False
logado = True

if ativo and logado: # precisa que as duas sejam verdadeiras, senão vai para o else
    print('Bem vindo usuário!')
else:
    print('Voce precisa ativar sua conta, cheque seu email.')

if ativo or logado: # precisa que pelo menos uma seja verdadeira, senão vai para o else
    print('Bem vindo usuário!')
else:
    print('Voce precisa ativar sua conta, cheque seu email.')

if not ativo: # se ativo for false, senão vai para o else
    print('Voce precisa ativar sua conta, cheque seu email.')
else:
    print('Bem vindo usuário!')

if ativo is True: # se ativo for True, senão vai para o else
    print('Bem vindo usuário!')
else:
    print('Voce precisa ativar sua conta, cheque seu email.')

print(ativo is False) # pergunta se ativo é False

nome = 'Pedro'

print(nome.isupper()) # pergunta se o nome inteiro é maiusculo
print(nome.istitle()) # pergunta se apenas a primeira letra do nome é maiusculo