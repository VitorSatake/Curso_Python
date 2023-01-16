"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parametro seja opcional;

def exponencial(numero, potencia=2): # coloca o 2 como padrao para a potencia
    return numero ** potencia

print(exponencial(3)) # nao precisa do segundo parametro, é opcional, pois esta como padrao 2
print(exponencial(3, 5)) # quando informa a potencia como argumento, utiliza o valor informado

# OBS : Se o usuario passar somente um argumento, este sera atribuido ao parametro numero, e sera calculado
# o quadrado desse numero
# Se o usuario passar 2 argumentos, o primeiro sera para numero e o segundo para potencia

# Se quiser que os dois valores sejam opcionais, é só atribuir um valor para o numero, igual a potencia

# Em funções Python, os parametros com valores padrao DEVEM sempre estar ao final da declaração

# Erro

def teste(num=2, potencia): 
    return num ** potencia

# Correto

def teste(potencia, num=2): 
    return num ** potencia

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que voce fosse o instrutor'
    return f'Ola {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Ozzy'))

# Porque utilizar paramatros com valor default?

# Nos permite ser mais flexivel nas funções
# Evita erros com parametros incorretos
# Nos permite trabalhar com exemplos mais legiveis de codigo

# Quais tipos de dados podemos utilizar como valores default para paarametros ?
# Qualquer tipo de dados
# Numeros, strings, floats, booleanos, listas, tuplas, dicionarios, funções etc.

# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def sub(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, sub))

# Escopo - Evitar problemas e confusões

# Variaveis globais
# Variaveis locais

instrutor = 'Geek' # Variavel Global

def diz_oi():
    instrutor = 'Python' # Variavel local, preferencia na utilização da função, se sobrepos a global, quando mesmo nome
    return f'Oi {instrutor}'

print(diz_oi())

def diz_oi():
    prof = 'Geek' # variavel local
    return f'Ola {prof}'

print(diz_oi())
print(prof) # nao reconhece fora da função, pois é local

# ATENÇAO com variaveis globais ( Se puder evitar, evite !)

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError (A variavel esta sendo utilizada para processamentosem ter sido inicializada(total=0 seria o certo))
    return total

print(incrementa())

# ATENÇAO com variaveis globais ( Se puder evitar, evite !)

total = 0

def incrementa():
    global total # avisando que queremos utilizar a variavel global
    total = total + 1 
    return total

print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que sao declaradas dentro de funções, e tambem tem uma forma especial de escopo de variavel

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())  # fica sempre em 1, porque toda vez que inicia, contador inicia em 0
print(fora())
print(fora())

print(dentro()) # função dentro só é reconhecido dentro da função fora

"""


