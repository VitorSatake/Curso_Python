"""
Escrevendo em arquivos CSV.

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

# writer() -> gera um objeto para que possamos escrever em um arquivo csv, utilizamos o metodo writerow()
# para escrever cada linha, esse metodo recebe uma lista.

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero do filme: ')
            duracao = input('Informe a duração do filme (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])


"""

# DictWriter
#OBS : As chaves do dicionario devem ser as mesmas utilizadas como cabeçalho

from csv import DictWriter

with open('filmes3.csv', 'a') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero do filme: ')
            duracao = input('Informe a duração do filme (em minutos): ')
            escritor_csv.writerow({"Titulo":filme, "Genero":genero, "Duracao":duracao})