"""
Recebendo dados do usuario.

input() = todo dado recebido via input é do tipo string

"""
#print("Qual seu nome ?")
#nome = input() # entrada do dado, atribuido a uma variavel
#mesma coisa com menos linha
nome = input('Qual o seu nome ?\n')

#Exemplo antigo de print
#print('Seja bem vindo(a) %s .' % nome.title()) # imprime a variavel do input, com title para letra maiuscula no começo
#Exemplo de print moderno
#print('Seja bem vindo(a) {0}.'.format(nome.title())) # novo modelo moderno de print
#Exemplo de print mais moderno
print(f'Seja bem vindo(a) {nome.title()}.') # novo modelo mais moderno de print

#mesma coisa com menos linha
#print("Qual sua idade ?")
#idade = input()
idade = int(input('Qual sua idade ?\n')) # ja transforma a string em int

#Processamento


#Saida de dados
#Exemplo antigo de print
#print('O(a) %s tem %s anos.' % (nome.title(), idade)) # imprime a variavel do input, com title para letra maiuscula no começo
#print('O(a) {0} tem {1} anos.'.format(nome.title(), idade)) # novo modelo de print
#Exemplo de print mais moderno
print(f'O(a) {nome.title()} tem {idade} anos.') # novo modelo mais moderno de print
#print(f'O(a) {nome.title()} nasceu em {2022 - int(idade)} e tem {idade} anos.') # int(idade) = cast == converte string em numero inteiro
print(f'O(a) {nome.title()} nasceu em {2022 - idade} e tem {idade} anos.') # print com a idade ja em int
