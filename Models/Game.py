from Models.Player import Player


class Game:
    player1: Player
    player2: Player | None
    name: str

    def __init__(self, name: str, player1: Player):
        self.player1 = player1
        self.player2 = None
        self.name = name

    def can_other_player_join(self):
        return self.player2 is None
