"""
Lendo arquivos CSV

CSV - Comma Separate Values - Valores separados por virgula

# Separador por virgula

1,2,3,4,5,6
'geek', 'university', 'python'

# Separador por ponto e virgula

1;2;3;4;5;6
'geek'; 'university'; 'python'

# Separador por espaço

1 2 3 4 5 6
'geek' 'university' 'python'

Site para conseguir dados:
http://dados.gov.br/dataset

"""

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    print(dados)

