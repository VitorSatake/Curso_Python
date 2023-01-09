"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionarios python sao conhecidos por Mapas.

Dicionarios sao coleções do tipo chave/valor.

Dicionarios sao representados por chaves {}.
print(type({}))

OBS: Tanto a chave quanto o valor podem ser de qualquer tipo de dado, chave e valor sao separados por :
'chave: valor'
Podemos misturar tipos de dados

# Criação de dicionarios

# Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'} # chave/valor
print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br= 'Brasil', eua= 'Estados Unidos')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['eua'])

# OBS: Caso acesse utlizando uma chave que nao existe, erro KeyError

# Forma 2 - Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru')) # nao retorna erro KeyError, retorna none

# Caso o get nao encontre o objeto com a chave informada, será retornado o valor None, e nao KeyError

pais = paises.get('br') 

if pais:
    print(f'Encontrei o pais {pais}.')
else:
    print('Nao encontrei o pais.')

# Podemos definir um valor padrao caso nao encontremos a chave informada

pais = paises.get('ru', 'Nao encontrado') # tenta achar o valor pedido, caso nao encontre, coloca o segundo

print(f'Encontrei o pais {pais}.')

# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive
# lista, tupla, dicionario, como chaves de dicionario

# OBS: Tupla por exemplo sao bastante interessantes de serem utilizadas como chaves de dicionario,
# pois as mesmas sao imutaveis

localidades = {
    (35.6895, 39.6917): 'Escritorio Tokio',
    (45.6895, 29.6917): 'Escritorio Nova York',
    (15.6895, 19.6917): 'Escritorio Sao Paulo'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350
print(receita)

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado) # memso que = receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)

# CONCLUSAO 1 : A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma
# CONCLUSAO 2 : Em dicionarios, NAO podemos ter chaves repetidas

# Remover dados de um dicionario

# Forma 1 - Mais comum

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

ret = receita.pop('mar')
print(ret)
print(receita)

# OBS 1 : Aqui precisamos sempre informar a chave, e caso nao encontre o elemento
# um KeyError é retornado
# OBS 1 : Ao removermos um objeto, o valor desse objeto é sempre retornado

# Forma 2

del receita['fev']
print(receita)

# OBS 2 : Neste caaso o valor removido nao é retornado
# OBS 2: Se a chave nao existir será gerado um KetError

# Imagine que voce tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

# Opção 1 - Poderiamos utilizar uma Lista para isso? SIM ! 

carrinho = []

produto1 = ['PlayStation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto

# Opção 2 - Poderiamos utilizar uma tupla para isso ? SIM !

produto3 = ('PlayStation 4', 1, 2300.00)
produto4 = ('God of War 4', 1, 150.00)

carrinho2 = (produto3, produto4)

print(carrinho2)

# Teriamos que saber qual é o indice de cada informação no produto

# Opção 3 - Poderiamos utilizar um dicionario para isso ? SIM !

carrinho3 = []

produto5 = {'nome': 'PlayStation 4', 'quantidade': 1, 'valor': 2300.00}
produto6 = {'nome': 'God of War 4', 'quantidade': 1, 'valor': 150.00}

carrinho3.append(produto5)
carrinho3.append(produto6)

print(carrinho3)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.

# Metodos de dicionarios:

# Limpar o dicionario (zerar dados)

d.clear()
print(d)

# Copiando um dicionario para outro

# print(dir({}))

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Forma 1 - Deep Copy

novo = d.copy() 
print(novo)

novo['d'] = 4 # cria nova chave valor 4, no novo, nao altera o d
print(novo)
print(d)

# Forma 2 - Shallow Copy - Ambos sao alterados

novo = d
print(novo)

novo['d'] = 4

print(novo)
print(d)

"""

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'} # chave/valor

# Forma nao usual de criação de dicionarios

outro = {}.fromkeys('a', 'b') # cria chave a, valor b

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')# atribui valor desconhecido para todos

print(usuario)
print(type(usuario))

# O metodo fromkeys recebe dois paraametros: um iteravel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave, e ira atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor') # para cada letra atribui o valor (valor), nao colocou o resto pq
# nao ha repetição de chave
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)