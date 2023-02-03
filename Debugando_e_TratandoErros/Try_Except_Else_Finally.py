"""
Try / Except / Else / Finally

Dica de  quando e onde tratar codigo:

TODA ENTRADA DEVE SER TRATADA !!!

OBS : A função do usuario é DESTRUIR seu sistema !

#num = 0 # declarar o valor 0 para iniciar como global, pq se der o erro a variavel nao tera sido criada, é uma forma

# Else -> é executado somente se nao ocorrer o erro.

try:
    num = int(input('Informe um numero: '))
except ValueError as err: 
    print(f'A aplicação gerou o seguinte erro: {err}!')
else:
    print(f'Voce digitou {num}.')

# Finally


try:
    num = int(input('Informe um numero: '))
except ValueError as err: 
    print(f'A aplicação gerou o seguinte erro: {err}!')
else:
    print(f'Voce digitou {num}.')
finally:
    print('Executando o finally.')
    
print('Depois do bloco try/except.')

# OBS : O bloco finaaly é SEMPRE executado, independente se houve exceção ou nao.

# O finally geralmente é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro numero: '))

try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto!')

# Exemplo mais complexo CORRETO

# OBS : Voce é responsavel pelas entradas das suas funções, entao trate-as !

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto!'
    except ZeroDivisionError:
        return 'Nao é possivel realizar uma divisao por 0!'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

# Exemplo mais complexo CORRETO -> GENERICO

# OBS : Voce é responsavel pelas entradas das suas funções, entao trate-as !

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:  # Forma generica
        return 'Ocorreu um problema!'



num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))
"""

# Exemplo mais complexo CORRETO -> SEMI-GENERICO

# OBS : Voce é responsavel pelas entradas das suas funções, entao trate-as !

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:  # Forma semi-generica
        return f'Ocorreu um problema: {err}!'



num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))
