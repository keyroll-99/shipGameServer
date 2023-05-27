import random

from Models.Player import Player


class Game:
    player1: Player
    player2: Player | None
    moving_player: Player | None
    game_phase = "init"
    name: str

    def __init__(self, name: str, player1: Player):
        self.player1 = player1
        self.player1.game_init()
        self.player2 = None
        self.name = name
        self.moving_player = None

    def can_other_player_join(self):
        return self.player2 is None

    def join(self, player: Player):
        if self.can_other_player_join():
            self.player2 = player
            self.player2.game_init()

    def set_game_phase(self):
        if self.player1.ready and self.player2.ready:
            self.game_phase = "game"
            rand = random.randint(0, 1)
            if rand == 0:
                self.moving_player = self.player1
            else:
                self.moving_player = self.player2

    def game_can_start(self):
        return self.player1 is None and self.player2 is None

    def get_game_data(self, player_name):
        player = self.player1 if self.player1.name == player_name else self.player2
        enemy = self.player2 if self.player1.name == player_name else self.player1
        response = {
            "name": self.name,
            "enemy_name": enemy.name,
            "player_board": player.player_board,
            "player_hit": player.player_hit,
            "enemy_hit": enemy.player_hit,
            "is_your_turn": player_name == self.moving_player.name if self.game_phase != "init" else None,
            "game_phase": self.game_phase,
        }

        return response

    def close_game(self):
        # todo what do when one of player exit
        pass
