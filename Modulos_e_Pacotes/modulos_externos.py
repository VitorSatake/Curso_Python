"""
Modulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Voce pode conhecer todos os pacotes externos oficiais em : https://pypi.org

Colorama -> é utilizado para permitir impressao de textos coloridos no terminal

Instalando um modulo:

pip install nome_do_modulo

# Utilizando o pacote instalado

# pip install colorama

from colorama import init
init()

from colorama import Fore, Back, Style

print(Fore.RED + 'Geek University')
print(Fore.GREEN + 'Geek University')
print(Fore.YELLOW + 'Geek University')

print('Geek University')
print('Geek University')
print('Geek University')

print(Style.RESET_ALL) # Reseta as configurações anteriores

print('Geek University')


print(Back.RED + 'Geek University')
"""

