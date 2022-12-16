"""
Loop While

Forma Geral

While espressão_booleana
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira

Expressão booleana, é todo expressão onde o resultado é verdadeiro ou falso
"""

# Exemplo 1
numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# Obs: em um loop while é importante que cuidemos do criterio de parada para nao causar um loop infinito

#Exemplo 2

resposta = '' # atribuindo uma string vazia para receber a resposta

while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')

# Exemplo de estrutura para checar se campo nome foi preenchido
nome = ''

while nome == '':
    nome = input('Digite seu nome:')
