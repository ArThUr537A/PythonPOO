# Crie a classe Gamer, onde podemos cadastrar
# nome, nick e os jogos favoritos de uma pessoa.
# Crie também um metodo que permita mostrar a ficha
# desse gamer.
from rich import print
from rich.panel import Panel
from rich.console import Group


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.games = []

    def add_favoritos(self, game):
        self.games.append(game)

    def ficha(self):
        gamesText = ""
        for c in range(0, len(self.games)):
            if c != (len(self.games) - 1):
                gamesText += f":video_game: [blue]{self.games[c]}\n"

            else:
                gamesText += f":video_game: [blue]{self.games[c]}"

        conteudo = Group(
            f"Nome real: [black on blue] {self.nome} ",
            f"Jogos favoritos:",
            gamesText
            )

        painel = Panel(conteudo, title=f"jogador <{self.nick}>", width=50)
        print(painel)

        # print(self.nome)
        # print(self.nick)
        # print(self.games)

j1 = Gamer("Fabricio da Silva", "detonador2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Olívia Souza", "peach_raivosa")
j2.add_favoritos("Mario Bros")
j2.add_favoritos("Call of Duty")
j2.ficha()

