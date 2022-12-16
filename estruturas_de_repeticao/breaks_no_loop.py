"""
Saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.

"""
#Exemplo 1

for numero in range(1, 11):
    if numero == 6: # quando numero for igual a 6 do range, faz o break e sai do loop
        break
    else:
        print(numero)

print('Sai do loop')

# Exemplo 2

while True: # criando um laço infinito para executar até digitar 'sair'
    comando = input("Digite 'sair' para sair : ")
    if comando == 'sair':
        break