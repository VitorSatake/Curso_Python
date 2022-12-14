"""
Estruturas lógicas e condicionais / IF , ELSE , ELIF


"""

idade = 20

if idade < 18: # se idade for menor que 18, faça print
    print('Menor de idade.')
elif idade == 18: # cria mais condicionais, quantas precisar, pra checar antes do else
    print("Sua idade é 18 anos.")
elif idade == 20: # cria mais condicionais, quantas precisar, pra checar antes do else
    print("Sua idade é 20 anos.")
else: # senão, checa o if, se nao for verdadeira, vai para o else
    print('Maior de idade.')
