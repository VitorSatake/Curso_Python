"""
Modulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta performance
"""
from collections import deque

# Criando deques

deq = deque('geek')

print(deq)

# Adicionando elementos no deque

deq.appendleft('j') # adiciona no começo, a esquerda
print(deq)
deq.append('o') # adiciona no final
print(deq)

# Remover elementos

print(deq.pop()) # remove e retorna o ultimo elemento

print(deq)

print(deq.popleft()) # remove e retorna o primeiro elemento

print(deq)
