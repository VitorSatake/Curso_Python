"""
Metodos de data e hora

import datetime

# Com now() podemos especificar um timezone (Fuso Horario)
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo a meia noite - combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))


# Encontrar o dia da semana - weekday()

# Os dias da semana do metodo weekday() começam e 0, sendo esta a segunda-feira
# 0 = segunda-feira (monday)
# 1 = terça-feira (tuesday)
# 2 = quarta-feira (wednesday)
# 3 = quinta-feira (thursday)
# 4 = sexta-feira (friday)
# 5 = sabado (saturday)
# 6 = domingo (sunday)


manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())

aniversario = input('Informe sua data de nasciemnto (dd/mm/yyy): ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma Segunda-Feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma Terça-Feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma Quarta-Feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma Quinta-Feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma Sexta-Feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em um Sabado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um Domingo')
    

# Formatando datas/horas com strftime() (String Format Time)
# brasil - dia/mes/ano  hora/minuto

hoje = datetime.datetime.today()

hoje_formatado = hoje.strftime('%d/%m/%Y') # brasil y minusculo = 2 digitos de ano/ Y maiusculo = 4 digitos de ano
hoje_formatado2 = hoje.strftime('%d/%B/%Y') # B maiusculo mostra mes por escrito/ b minusculo abreviado escrito

print(hoje_formatado)
print(hoje_formatado2)


# Função para gerar data em portugues pelo now() recebendo la embaixo

def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'
    


# Formatando datas/horas com strftime() (String Format Time)
# brasil - dia/mes/ano  hora/minuto

hoje = datetime.datetime.today()

print(formata_data(hoje))


import datetime
from textblob import TextBlob

# Refatorando a função aanterior

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()

print(formata_data(hoje))

import datetime


nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual sua data de nascimento ? (dd/mm/yyy)')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)


import datetime


# somente hora

almoço = datetime.time(12, 30, 0)

print(almoço)

import timeit

# marcando tempo de execução do codigo com timeit

# Loop for

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000) 
print(tempo)


# List Comprehension

tempo2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000) 

# Map

tempo3 = timeit.timeit('"-".join(map(str, range(100)))', number=10000) 
"""

import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4 #  ** elevado
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000)) # tempo de execução
