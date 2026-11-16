# Crie a classe Caneta, que simule o funcionamento
# de uma caneta colorida, podendo escrever frases
# na cor relativa
from rich import print


class Caneta:
    def __init__(self, cor):
        if cor == "azul":
            self.cor = "blue"
        if cor == "vermelha":
            self.cor = "red"
        if cor == "verde":
            self.cor = "green"
        if cor == "amarelo":
            self.cor = "yellow"
        if cor == "laranja":
            self.cor = "orange"
        if cor == "roxo":
            self.cor = "purple"
        self.tampa = True
    def destampar(self):
        self.tampa = False

    def escrever(self, texto):
        if self.tampa:
            print(fr":no_entry_sign: A [{self.cor}]caneta[/] está tampada!")
        else:
            print(f"[{self.cor}]{texto} ", end="")

    def quebrar_linha(self, num):
        for c in range(0, num):
            print("")

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")
#
# c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto")
c3.escrever("Vamos exercitar!")