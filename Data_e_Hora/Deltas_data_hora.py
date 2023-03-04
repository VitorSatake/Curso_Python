"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyy 12:55:34.456787
data_final = dd/mm/yyy 13:34:34.456787

delta = data_final - data_inicial

import datetime

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2023, 11, 17, 0)

# Calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(tempo_para_evento.days) # quantos dias apenas

print(f'Faltam {tempo_para_evento.days} dias e {tempo_para_evento.seconds // 60 // 60} horas para o meu aniversario!')

"""

import datetime

# Criando uma regra para vencimento de pagamento de boleto, gerando data da compra e quando dias para pagar o boleto
data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)