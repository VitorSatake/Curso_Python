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

# Podemos checar ssse um diretorio é absoluto ou relativo

print(os.path.isabs('D:\\Curso_Python_Geek'))

# OBS para usuarios Windows:

# Se você tiver utilizando um computador com Windows, deverá ter cuidado para verificar diretórios !!!


# Podemos identificar o sistema operacional com o modulo os

#print(os.name) # posix (linux e mac) , nt (Windows)

# Podemos ter mais detalhes do sistema operacional

#print(os.uname()) # para linux

import sysconfig

print(sysconfig)

print(sysconfig.get_platform())

import sys

print(sys.platform)

print(sys.version)

print(sys.executable)
"""
# Fazer o import

import os

