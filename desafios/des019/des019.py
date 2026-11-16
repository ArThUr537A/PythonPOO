# Crie a classe Livro, que vai simular a passagem de páginas
# de um livro, considerando também se o usuário chegou ao
# fim da leitura

from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagatual = 1
        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{titulo}[/]' que tem [green]{paginas} páginas[/] no total. Você agora está na [yellow]pagina 1[/][/blue]")


    def avancar_paginas(self, avancarpg):


        self.pagatual = avancarpg + self.pagatual
        print(avancarpg, self.pagatual)


#FALTA COLOCAR O LIMITE DE PÁGINAS DO LIVRO



l1 = Livro("10 Coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(5)
l1.avancar_paginas(3)




