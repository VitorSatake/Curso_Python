"""
Manipulando Data e Hora

Python tem um modulo built-in (integrado) para trabalhar com data e hora chamado datetime

import datetime

#print(dir(datetime))

print(datetime.MAXYEAR) # ano maximo que suporta
print(datetime.MINYEAR) # ano minimo que suporta

print(datetime.datetime.now()) # retorna a data e hora corrente 2023-03-04 16:21:07.069697

# datetime.datetime(year, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now())) 

#replace() para fazer ajustes na data e hora

inicio = datetime.datetime.now()

# Alterar o horario para 16 horas 0 minutos 0 segundo 0 microsegundo

inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0) # sobrescrevendo inicio

print(inicio)

# Recebendo dados do usuario e convertendo para data

evento = datetime.datetime(2024, 1, 1, 0)

print(type(evento)) # class datetime

print(type('31/12/23')) # class string

print(evento)

nascimento = input('Informe sua data de nasciemnto (dd/mm/yyy): ')

nascimento = nascimento.split('/') # array separando por /

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))
"""
import datetime


evento = datetime.datetime.now()


# Acesso individual dos elementos de data e hora

print(evento.year) # ano
print(evento.month) # mês
print(evento.day) # dia
print(evento.hour) # hora
print(evento.minute) # minuto
print(evento.second) # segundo
print(evento.microsecond) # microsegundo

print(dir(evento))