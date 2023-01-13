"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, ja sabemos que temos funções que :
- Nao possuem entrada;
- Nao possuem saída;
- Possuem entrada mas nao possuem saída;
- Nao possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())

def quadrado_de_numero(numero):
    #return numero * numero
    return numero ** 2 # elevado ao quadrado

print(quadrado_de_numero(4))
print(quadrado_de_numero(5))
print(quadrado_de_numero(9))

# Refatorando a Função

def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}')

cantar_parabens('Pedro')
cantar_parabens('Joao')
cantar_parabens('Ricardo')

# OBS : Funções podem ter N parametros de entrada, ou seja, podemos receber como entrada em uma função
# quantos parametros forem necessarios, seprados por virgula

def soma(a, b):
    return a + b

print(soma(3, 7))
print(soma(2, 6))
print(soma(9, 9))

def multiplica(num1, num2):
    return num1*num2

print(f'\n{multiplica(7, 6)}')
print(f'{multiplica(3, 5)}')
print(f'{multiplica(9, 9)}')

def outra(num3, b, msg):
    return (num3 + b) * msg

print(f'\n{outra(3, 7, 5)}')
print(f'{outra(2, 5, 6)}')
print(outra(1, 7, 'Teste'))
print(outra(2, 7, 'Python'))

# OBS : Se a gente informar um numero errado de paraametro ou argumentos, teremos TypeError

# Nomeando parâmetros

def nome_completo(string1, string2): # melhorar o nome dos parametros
    return f'Seu nome completo é {string1} {string2}'

print(nome_completo('Pedro', 'Correa'))

def nome_completo_certo(nome, sobrenome): # melhorar o nome dos parametros
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Paulo', 'Silva'))

# A diferença entre Parametros e Argumentos

# Parametros sao variaveis declaradas na definição de uma função; def nome_completo_certo(nome, sobrenome)
# Argumento sao dados passados durante a execução de uma função; print(nome_completo('Paulo', 'Silva'))

# A ordem do parametros importa!!!

nome = 'Bruno'
sobrenome = 'Silva'

print(nome_completo(sobrenome, nome)) # colocando na ordem errada vai imprimir na ordem errada

# Argumentos Nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parametros nos argumentos para informa-los, podemos utilizar qualquer ordem

print(nome_completo_certo(nome=nome, sobrenome=sobrenome))
print(nome_completo_certo(sobrenome=sobrenome, nome=nome))
print(nome_completo_certo(sobrenome='Silva', nome='Bruno'))
"""

# Erro comum na utilização do Return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]



print(soma_impares(lista))

def armazena_impares(numeros):
    total = []
    for num in numeros:
        if num % 2 != 0:
            total.append(num)
    return total

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(armazena_impares(lista2))

