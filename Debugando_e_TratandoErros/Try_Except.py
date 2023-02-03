"""
O bloco Try/Except

Utilizamos o bloco Try/Except para tratar erros que podem ocorrer no nosso codigo.
Prevenindo assim que o programa pare de funcionar e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problematica
except:
    //oque deve ser feito em caso de problemas

# Exemplo 1 - Tratando um erro generico (pega qualquer tipo de erro)

try: 
    geek() # NameError
except:
    print('Deu algum problema!')

# Tente executar a função geek(), caso voce encontre erros, imprima a mensagem de erro

# Exemplo 2 - Tratando um erro generico (pega qualquer tipo de erro)

try: 
    len(5) # TypeError
except:
    print('Deu algum problema!')

# Tente executar a função geek(), caso voce encontre erros, imprima a mensagem de erro

OBS : Tratar erro de forma generica, nao é a melhor forma de tratamento de erros. 
O ideal é SEMPRE tratar de forma especifica !

# Exemplo 3 - Tratando um erro especifico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente!')

# Exemplo 4 - Tratando um erro especifico

try:
    len(5)
except NameError:
    print('Você está utilizando uma função inexistente!')
# Nao resolve pois o erro é TypeError, e esta sendo passado o except como NameError

# Exemplo 5 - Tratando um erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err: # Da umn apelido de err para TypeError, e passa no print
    print(f'A aplicação gerou o seguinte erro: {err}!')

# Podemos efetur diversos tratamentos de erros de uma vez

try:
    #len(5) # TypeError
    #geek() # NameError
    print('Geek'[9]) # IndexError
except NameError as erra: 
    print(f'Deu NameError: {erra}!')
except TypeError as errb:
    print(f'Deu TypeError: {errb}!')
except:
    print('Deu um erro diferente!') # Caso passe por todos os outros erros conhecidos, tratando de forma generica
"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {'nome': 'Geek'}

print(pega_valor(dic, 'game')) # KeyError, tratado no try/except na função pega_valor()







