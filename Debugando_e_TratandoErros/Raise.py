"""
Levantando os proprios erros com raise

raise -> lança exceções

OBS : O raise nao é uma função, é uma palavra reservada, assim como def ou qualquer outra em python.

Para simplificar, pense no raise como sendo util para que possamos criar nossas proprias exceções e 
mensagens de erro.

A forma geral de utilização é :

raise TipoDoErro('Mensagem de erro')

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'Azul') # forma correta

#colore('Geek', 4) # gera a mensagem de erro (raise), pois 4 nao é string

colore(True, 'Azul') # gera a mensagem de erro (raise), pois True nao é string

# Exemplo real refatorado

def colore(texto, cor):
    cores = ('verde', 'amaarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'verde') # forma correta

colore('Geek', 'preto') # gera a mensagem de erro (raise) após conferir os ifs, pois 'preto' nao está na lista cores

OBS : O raise assim como o return, finaliza a função, ou seja, nada após o raise é executado
"""

# Exemplo real

def colore(texto, cor):
    cores = ('verde', 'amaarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'verde') # forma correta

colore('Geek', 'preto') # gera a mensagem de erro (raise) após conferir os ifs, pois 'preto' nao está na lista cores