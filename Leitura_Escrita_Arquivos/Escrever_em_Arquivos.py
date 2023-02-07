"""
Escrevendo em arquivos

OBS : Ao abrir um arquivo para leitura, nao podemos realizar a escrita nele, apenas ler.
Da mesma forma se abrirmos um arquivo para escrita, nao podemos ler, apenas escrever nele.

OBS : Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para esrevermos dados em um arquivo, apos abrir o arquivo utilizamos a funçaõ write().
Esta função recebe uma string como parametro, caso contrario, teremos um TypeError.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo nao existir será criado.
Caso ele ja exista, o anterior será apagado e um novo será criado. Dessa forma, todo o conteudo
no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write - escrita

# Forma Pythonica

with open('novo.txt', 'w', -1, 'utf-8') as arquivos: # mudando para utf-8 para receber acentos
    arquivos.write('Novos dados.\n')
    arquivos.write('Podemos colocar quantas linhas quisermos.\n')
    arquivos.write('Esta é a ultima linha.\n')

with open('geek.txt', 'w', -1, 'utf-8') as arquivo:
    arquivo.write('Geek\n' * 1000)


# Forma tradicional de escrita em arquivo, nao Pythonica.

arquivo = open('mais.txt', 'w', -1, 'utf-8')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Outra linha escrita.\n')

arquivo.close()
"""
with open('frutas.txt', 'w', -1, 'utf-8') as arquivo:  
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n') #pulando linha
        else:
            break
    



