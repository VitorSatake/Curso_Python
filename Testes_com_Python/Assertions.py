"""
Assertions (Afirmações/Checagens/Questionamentos)


Em python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é valida ou nao.
Se a expressao for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError.

# OBS : Nos podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem
de erro personalizada.

# OBS : A palavra 'assert' pode ser utilizada em qualquer função ou codigo nosso, ou seja,
nao precisa ser exclusivamente nos testes.

# ALERTA : Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parametro -O, nenhum 'assert' sera validado, ou seja, todas suas validações ja eram.
"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos numeros precisam ser positivos!'
    return a + b

#print(soma_numeros_positivos(2, 7))
ret = soma_numeros_positivos(2, 4) # 6
#ret = soma_numeros_positivos(-2, 4) # AssertionError
print(ret)

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata-frita',
        'cachorro-quente'
    ], 'A comida precisa ser fast food.'
    return f'Estou comendo {comida}.'

comida = input('Informe a comida: ')
print(comer_fast_food(comida))

# ALERTA : Cuidado ao utilizar 'assert'

