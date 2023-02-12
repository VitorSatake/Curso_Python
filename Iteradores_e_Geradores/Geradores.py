"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS : O contrario nao é verdadeiro, ou seja, nem todo iterator é um generator.

Outras Informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressoes Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

--------------------------------------------------------------------------------
| Funções                              | Generator Functions
--------------------------------------------------------------------------------
| utilizam return                      | utilizam yield
--------------------------------------------------------------------------------
| retorna uma vez                      | podem utilizar yield multiplas vezes
--------------------------------------------------------------------------------
| quando executada, retorna um valor   | quando executada retorna um generator
--------------------------------------------------------------------------------


gen = conta_ate(5)

for num in gen:
    print(num)


#print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(next(gen)) # 1

print('Geek') # para separaar


for num in gen: # começa do 2 pq teve um next antes
    print(num)

"""

# Exemplo de Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS : Uma Generator Function nao é um Generator. Ela gera um Generator.

gen = list(conta_ate(10))

print(gen) # ja faz o next todas as vezes possiveis e colocados na lista
