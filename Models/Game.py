from Models.Player import Player


class Game:
    player1: Player
    player2: Player
    name: str

    def __init__(self, name: str, player1: Player):
        self.player1 = player1
        self.name = name
