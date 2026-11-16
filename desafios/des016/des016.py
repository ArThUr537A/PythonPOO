# Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo.
# Crie também um método que permita ao funcionário se apresentar.

# definindo a classe
from rich import print


class Funcionario:
        
    # definindo os atributos
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    # definindo o método
    def apresentacao(self):
        return f":handshake: Olá, eu sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa Curso em Vídeo"

# instanciando classe e apresentando dados   
c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())
