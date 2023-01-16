""" 
Documentando Funções com Docstrings

"""
# Exemplos

def diz_oi():
    """Uma função simples que retorna a string Oi"""
    return 'Oi !'

#print(diz_oi.__doc__) # uma forma de acessar o DocString da função

# Podemos ter acesso a documentação de uma função em Python utilizando a propriedade especial __doc__
# Podemos ainda fazer acesso a documentação com a função help()  print(help(diz_oi))

"""
from DocStrings import diz_oi # import para abrir o Docstring

print(diz_oi())
print(help(diz_oi)) # uma forma de acessar o DocString da função
print(diz_oi.__doc__) # outra forma de acessar o DocString da função
"""

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencia' informada.
    :param numero: Numero que desejamos gerar o exponencial.
    :param potencia: Potencia que queremos gerar o exponencial. Por padrao é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia

#print(exponencial.__doc__)
print(help(exponencial))