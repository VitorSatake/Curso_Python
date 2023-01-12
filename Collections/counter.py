"""
Modulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes (tipos de dados de containr de alta performance)

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo Collections Counter que é parecido
com um dicionario, contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iteravel, aqui usamos uma lista
lista = s = [1, 1, 2, 2, 3, 4, 5, 5, 5, 1, 1, 4, 4, 5, 5, 3, 3, 2]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Counter({5: 5, 1: 4, 2: 3, 3: 3, 4: 3})
# Veja que para cada elemento da lista , o Counter criou uma chave e colocou como valor a quantidade de ocorrencias

# Exemplo 2

print(Counter('Geek University'))

# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
# Criou uma chave para cada letra e o valor a quantidade de ocorrencias, incluindo o espaço (1)


"""
# Realizando o import

from collections import Counter

# Exemplo 3

texto = """ Em informática, o web wiki ([wiki], do havaiano "super veloz") é uma linguagem de marcação utilizada 
em website que contém hipertexto e hiperligações que trabalham com o software wiki, no qual os usuários 
modificam colaborativamente o seu conteúdo e a estrutura diretamente usando um navegador web, editado com 
a ajuda de um editor de texto enriquecido.[1]

O software wiki, é um tipo de sistema de gestão de conteúdo, mas diverge da maioria dos outros tais sistemas, 
inclusive software de blog, em que o conteúdo é criado sem qualquer dono ou líder definido."""

palavras = texto.split() # faz do texto uma lista, separando as palavras como elementos
#print(palavras)

res = Counter(palavras) # gera cada palavra como chave e o valor a quantidade de ocorrencias
print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto

print(res.most_common(5)) 
