"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

Oque são testes unitários ?

Teste Unitario é a forma de se testar unidades individuais de codigo fonte.

Unidades individuais podem ser : funções, metodos, classes, modulos etc.

#OBS : Teste Unitário nao é especifico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir dde então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para a sua unidade.

# Conhecendo as assertions
https://docs.python.org/3/library/unittest.html

Metodo                    Checa que
assertEqual(a,b)          a == b
assertNotEqual(a,b)       a != b
assertTrue(x)             x é verdadeiro
assertFalse(x)            x é falso
assertIs(a,b)             a é b
assertIsNot(a,b)          a não é b
assertIsNone(x)           x é None
assertIsNotNone(x)        x não é None
assertIn(a,b)             a está em b
assertNotIn(a,b)          a não está em b
assertIsInstance(a,b)     a é instancia de b
assertNotIsInstance(a,b)  a não é uma instancia de b


Por convenção todos os testes em um test case, devem ter seu nome iniciado cpm test_


Para executar os testes com unittest

python nome_do_modulo.py

Para executar os testes com unittest no modo verbose (mais detalhado)

python nome_do_modulo.py -v

# Docstrings nos testes

Podemos acrescentar (e é recomendado) docstrings nos nossos testes
"""

# Pratica - Utilizando a abordagem TDD

