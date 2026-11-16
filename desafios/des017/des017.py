# Crie a classe Produto, onde podemos cadastrar nome e o preço.
# Crie também um método que mostra uma etiqueta de preço do produto

from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.console import Group


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def etiqueta(self):
        strpreco = str(self.preco)   
        tampreco = len(strpreco)     
                       
        conteudo = Group(
            Align.center(self.nome),
            Align.center("-" * 46),
            Align.center("-"*(int((46 - tampreco)/2 - 2)) + f"R${self.preco}" + "-"*int((46 - tampreco)/2))
        )

        return Panel(conteudo, title="Produto", width=50)

p1 = Produto("Iphone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

print(p1.etiqueta())
print(p2.etiqueta())   
