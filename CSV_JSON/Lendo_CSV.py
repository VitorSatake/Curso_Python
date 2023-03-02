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

# Possivel de se trabalhar, mas nao éo ideal (trabalhoso)
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    #print(type(dados))
    dados = dados.split(',')[2]
    print(dados)

    
A linguagem pythonpossui duas formas diferentes para ler dados em arquivos csv:
    - reader -> permite que iteremos sobre as linhas do arquivo csv como listas;
    - DictReader -> permite que iteremos sobre as linhas do arquivo csv como OrderedDicts;


# Reader

from csv import reader

with open("lutadores.csv") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        # cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros.')


# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centimetros.")
"""


# DictReader com outro separador

from csv import DictReader

with open('filmes.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # cada linha é um OrderedDict
        #print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centimetros.")
        print(leitor_csv)