"""
Modulo Collections - Default Dict

# Recap Dicionarios

dicionario = {'curso': 'Programação em Python'}

print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) # KeyErro (quando nao encontra)

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor sera utilizado sempre que nao hpuver
um valor definido. Caso tentemos acessar uma chave que nao existe, essa chave sera criada e o valor
default sera atribuido.

OBS: Lambdas sao funçoes sem nome, que podem ou nao receber parametros de entrada 
e retornar valores
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programação em Python'

print(dicionario)

print(dicionario['outro']) # aqui nao apresenta KeyError, aparece valor 0 e cria a chave 'outro'

print(dicionario)