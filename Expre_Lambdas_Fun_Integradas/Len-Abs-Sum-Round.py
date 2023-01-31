"""
Len, Abs, Sum Round

# Len

len() -> retorna o tamanho(ou seja, o numero de itens) de um iteravel

# Só para revisar

print(len('Geek University')) # numero de caracteres
print(len([1,2,3,4,5])) # numero de variaveis

# Por debaixo dos panos, quando utilizamos função len() o python faz o seguinte:

# Dunder len  (dunder = funçoes com 2 _)
print('Geek University'.__len__())

# Abs

abs() -> retorna o valor absoluto de um numero inteiro ou real, de forma basica seria o seu valor real sem o sinal

# Exemplo abs()

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Sum

sum() -> recebe como parametro um iteravel, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial
#OBS : o valor inicial default = 0

print(sum([1,2,3,4,5]))

print(sum([1,2,3,4,5], 5)) # com valor inicial de 5

print(sum({'a': 1, 'b':5}.values())) # para somar apenas os valores em um dicionario

# Round

round() -> retorna um numero arredondado para n digito de precisao apos a casa decimal. Se a precisao nao for informada
retorna o inteiro mais proximo da entrada
"""

# Exemplos round()

print(round(10.2)) # arredonda para baixo
print(round(10.3)) # arredonda para baixo
print(round(10.7)) # arredonda para cima
print(round(10.2345)) # arredonda para baixo
print(round(10.2121, 2)) # com duas casas decimais de precisao, arredonadado para baixo
print(round(10.2199, 2)) # com duas casas decimais de precisao, arredonadado para cima
print(round(10.23456789, 4)) # com quatro casas decimais de precisao