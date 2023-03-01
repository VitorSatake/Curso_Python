"""
POO - Metodos Magicos

Metodos Magicos sao todos os metodos que utilizam dunder.

dunder init -> __init__ (construtor)

def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

Dunder -> Double Underscore

__repr__ -> representação do objeto

    def __repr__(self): 
        return f'{self.titulo} escrito por {self.autor}'


"""

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self): # preferencia entre os metodos de representação
        return self.titulo
    
    def __len__(self):
        return self.paginas
    
    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memoria.')

livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligencia Artificial!', 'Geek University', 350)

print(livro1)
print(livro2)

print(len(livro1))
