"""
Teste de Memoria com Generators

Sequencia Fibonacci
1, 1, 2, 3, 5, 8, 13 ... Soma dos dois ultimos numeros

# Função usando Listas  /  449 MB
def fib_lista(max):
    nums = []
    a, b, = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fib_lista(100): # em um for para ficar um embaixo do outro/ Teste memoria 449 MB
    print(n)


print(fib_lista(100)) # em um print para ficar em uma lista em sequencia
"""


# Função usando Geradores / 3 MB

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Teste 2  Geradores / 3 MB

for n in fib_gen(100):
    print(n)