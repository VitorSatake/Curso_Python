"""
Doctests


Doctests que colocamos na Docstring das funções/metodos python.

def soma(a, b):
    soma os numeros a e b
    #
    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    #
    return a + b

Para rodar um teste do doctest:

python -m doctest -v nome_do_modulo.py

Saida:

Trying:       
    soma(1, 2)
Expecting:    
    3
ok
1 items had no tests:
    Doctests
1 items passed all tests:
   1 tests in Doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

Com saida errada do esperado :

Trying:        
    soma(12, 2)
Expecting:     
    3
**********************************************************************
Failed example:
    soma(12, 2)
Expected:
    3
Got:
    14
1 items had no tests:
    Doctests
**********************************************************************
1 items had failures:
   1 of   1 in Doctests.soma
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.
"""

# Outro exempo aplicando o TDD

def duplicar(valores):
    """duplica os valores em uma lista
    
    >>> duplicar([1,2,3,4])
    [2,4,6,8]

    >>> duplicar([])
    []

    >>> duplicar(['a','b','c'])
    ['aa','bb','cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeRrror: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]

