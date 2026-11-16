# Crie a classe Churrasco, onde seja possível informar quantas pessoas vão 
# participar e mostre quanto de carne deve ser comprado, o custo total do 
# churrasco e o preço por pessoa


from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.console import Group

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
        

    def analisar(self):
        conspadrao = 0.4
        precokg = 82.40
        
        #calculo
        kgcompra = self.quant*conspadrao
        custototal = kgcompra*precokg
        precopessoa = conspadrao*precokg
        
        conteudo = Group(
            f"Analisando [green]{self.titulo}[/] com [blue]{str(self.quant)} convidados[/]",
            f"Cada participante comerá {conspadrao}Kg e cada Kg custa R${precokg:.2f}",
            f"Recomendo [blue]comprar {kgcompra:.3f}Kg[/] de carne",
            f"O custo total será de [green]R${custototal:.2f}[/]",
            f"Cada pessoa pagará [yellow]R${precopessoa}[/] para participar."
        )
        
        return Panel(conteudo, title=self.titulo, width=100)

p1 = Churrasco("Churras dos amigos", 15)
print(p1.analisar())
        
        



# Consumo padrão: 400g por pessoa
# Preço: R$82,40 /kg
