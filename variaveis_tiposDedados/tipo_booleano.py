"""
Tipo Booleano

Algebra booleano, sendo verdadeiro ou falso (True or False)

Sempre com a primeira letra maiuscula

Errado: true, false

Certo: True, False
"""
# exemplo de False
num = 5
print(num == 7)

# exemplo True
nome = 'Paulo'
print(nome == 'Paulo')

#Negação (not)
ativo = True
print(not ativo) # sempre o contrario

# Ou (or)
# pelo menos um de dois valores deve ser verdadeiro
#True ou True = True
#True ou False = True
#False ou True = True
#False ou False = False

ativo2 = True
logado = False

print(ativo or logado) # pelo menos um é verdadeiro 

# E (and)
# Tambem depende de dois valores, ambos os valores devem ser verdadeiros
#True ou True = True
#True ou False = False
#False ou True = False
#False ou False = True

ativo3 = True
logado2 = False

print(ativo3 and logado2) # um é verdadeiro e o outro e falso