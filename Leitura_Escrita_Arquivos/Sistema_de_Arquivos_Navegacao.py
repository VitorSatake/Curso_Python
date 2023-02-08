"""
Sistemas de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso 
do modulo OS.

os -> Operating System - Sistema Operacional

# Fazer o import

import os

# getcwd() -> pego o current work directory -> diretório de trabbalho corrente (atual)
# retorna o path (caminho) absoluto

print(os.getcwd())

# Para mudar o diretorio podemos utilizar o chdir()

os.chdir('..')
print(os.getcwd())
"""

