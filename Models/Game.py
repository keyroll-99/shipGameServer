import random

from Models.Player import Player


class Game:
    player1: Player | None
    player2: Player | None
    moving_player: Player | None
    game_phase = "init"
    winning_player_name = ""
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
            "player_turn_name": self.moving_player.name if self.moving_player is not None else None,
            "game_phase": self.game_phase,
            "winning_player_name": self.winning_player_name
        }

        return response

    def move(self, player: Player, hit_place):
        if player.name != self.moving_player.name:
            return

        is_player_one = True if player.name == self.player1.name else False
        other_player = self.player1 if not is_player_one else self.player2
        should_change_player = True

        if other_player.player_board[hit_place[1]][hit_place[0]] is not None:
            other_player.player_board[hit_place[1]][hit_place[0]] = "x"
            self.moving_player.player_hit[hit_place[1]][hit_place[0]] = 'x'
            should_change_player = False
            self.verify_result(other_player.player_board, player.name)
        else:
            self.moving_player.player_hit[hit_place[1]][hit_place[0]] = '-'

        if is_player_one and should_change_player:
            self.moving_player = self.player2
        elif should_change_player:
            self.moving_player = self.player1

    def verify_result(self, enemy_board, player_name):
        player_won = True
        for row in enemy_board:
            for col in row:
                if col is not None and col != 'x' and col != '-':
                    player_won = False

        if player_won:
            self.game_phase = "end"
            self.winning_player_name = player_name

    def close_game(self):
        self.game_phase = 'exit'

    def remove_player(self, player_name):
        if self.player1.name == player_name:
            self.player1 = None
        elif self.player2.name == player_name:
            self.player2 = None

    def can_remove(self):
        return self.game_phase == "end" and self.player2 is None and self.player1 is None
