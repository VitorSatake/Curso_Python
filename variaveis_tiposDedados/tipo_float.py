"""
Tipo float ou tipo real ou tipo decimal

Como a linguagem é baseada no idioma ingles, o separador de casas é ponto e nao virgula, exemplo :
5.5 e nao 5,5
"""
#errado
valor = 1,33

print(valor)

#certo

valor2 = 1.33

print(valor2)

valor3, valor4 = 1, 44 # é possovel fazer dupla atribuição de valor
print(valor3, valor4)
print(valor3)
print(valor4)

#numero complexo

num = 5j # com o j é numero complexo

print(type(num))




