"""
Mapas -> Conhecidos em python como dicionarios.

Dicionarios em python sao representados por chaves {}

# Iterar sobre dicionraios

for chave in receita:
    print(chave)

for valor in receita:
    print(receita[valor])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves

print(receita.keys()) # traz as chaves do dicionario

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values()) # traz os valores do dicionario

for valor in receita.values():
    print(valor)
"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Desempacotamento de dicionarios

print(receita.items())

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')


# Soma* , Valor Maximo*, Valor Minimo* , Tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))





