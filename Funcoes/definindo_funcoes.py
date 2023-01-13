"""
Definindo Funções 

- Funções sao pequenas partes de codigo que realizam tarefas especificas;
 - Pode ou nao receber entradas de dados e retornar uma saida de dados;
 - Muito uteis para executar procedimentos similares por repetidas vezes;

OBS : Se voce escrever uma função que realiza varias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos varias funçoes desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;



"""

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando uma função integrada (Built-in) do Python print()

print(cores)

# DRY : Don't Repeat Yourself  -  Não Repita voce mesmo / Nao repita seu código

# Como definir funções ?
# Em Python a forma geral de definir função é :
# def nome_da_função(parametros_de_entrada):
#    bloco_da_função

# Onde: nome_da_funcao -> SEMPRE, com letras minusculas, e se fo composto, separado po underline(Snake Case)
# parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um seprado por virgula, podendo ser opcional ou nao
# bloco_da_função -> Tmabem chamado de corpo da funçao ou implementação, é onde o processamento da função acontece.
# Neste bloco, pode ter ou nao retorno da função.

# OBS : Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python
# que estamos definindo uma função. Tambem abrimos o bloco de codigo com o ja conhecido dois pontos(:)
# que é utilizado em Python para definir blocos

# Definindo a primeira função 

def diz_oi():
    print('Oi!')

# OBS: 
# 1 - Veja que dentro das nossas funções podemos utilizar outras funções;
# 2 - Veja que nossa função só executa uma tarefa, ou seja, a unica coisa que ela faz é dizer oi;
# 3 - Veja que esta função nao recebe nenhum parametro de entrada;
# 4 - Veja que esta função nao retorna nada;

# Utilizando funções, chamada de execução

diz_oi()

# OBS : ATENÇÃO: Nunca esqueça de utilizar o parenteses () ao executar uma função
# ERRADO = diz_oi   CERTO = diz_oi()

# Exemplo 2

def cantar_parabens():
    print('Parabens pra voce')
    print('Nesta data querida')
    print('Muitas felicidades')

cantar_parabens()

for n in range(5): # cria o loop para repetir 5 vezes (0,1,2,3,4)
    cantar_parabens()

# Em Python podemos inclusive criar variaveis do tipo de uma função e executar esta função atraves da variavel

canta = cantar_parabens

canta()