"""
Ranges

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatoria,
mas sim de forma especificada.

Formas gerais:

range(valor_de_parada)

Obs: valor_de_parada não inclusive
"""
#Forma 1

for num in range(11): # printa de 0 - 10 .. o 11 não conta
    print(num)

#Forma 2
# rang(valor_de_inicio, valor_de_parada)

for num in range(1, 11): # printa de 1 - 10, pq foi dado inicio em 1 .. o 11 não conta
    print(num)

#Forma 3
# range(valor_de_inicio, valor_de_parada, passo), passo especificado pelo usuario

for num in range(1, 11, 2): # printa de 1 - 10, pq foi dado inicio em 1 .. o 11 não conta, e printa de 2 em 2, que é o passo
    print(num)

for num in range(0, 55, 5): # outro exemplo, inicio 0, até 50, de 5 em 5
    print(num)

#Forma 4 (igual a forma 3, mas inversa)
# range(valor_final, valor_de_parada, passo), valor final epasso especificado pelo usuario

for num in range(10, -1, -1): # coloca o passo como negativo para decrementar
    print(num)

lista = list(range(10)) # converte o rangede valor especificado, em uma lista
print(lista)