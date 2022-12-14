"""
Tipo String
 Dado tipo string:

 -Estiver em aspas simples -> 'uma string', '123', 'True', 'a'
  -Estiver em aspas duplas -> "uma string", "123", "True", "a"
   -Estiver em aspas simples triplas -> '''uma string''', '''123''', '''True''', '''a'''
    -Estiver em aspas duplas triplas -> 
"""

x = 'Teste de string'
print(type(x))
print(x.lower()) # deixa tudo minusculo
print(x[0:5]) # imprime por posição de vetor da string, slice de string

x2 = '123'
print(type(x))

x3 = "Teste de string"
print(type(x))
print(x3.upper()) # deixa tudo maiusculo

# Separa as palavras em uma lista
x4 = "Teste de separar string"
print(x4.split())
print(x4.split()[2]) # após separar em uma lista, imprime pela posição de palavra
print(x4[::-1]) # começa do primeiro elemento, vá até o ultimo elemento e inverta
print(x4.replace('G', 'P')) # troca letra G por P
print(x4.replace('e', 'P')) # troca todas as letras e por P