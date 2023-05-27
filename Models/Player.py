class Player:
    name: str = ""
    hit_target = 0
    lost_target = 0
    player_board = []
    player_hit = []
    ready = False

    def __init__(self, name):
        self.name = name

    def game_init(self):
        self.hit_target = 0
        self.lost_target = 0
        self.player_board = []
        self.player_hit = [[0] * 10 for _ in range(10)]
        self.ready = False

    def set_is_ready(self, playerBoard):
        self.ready = True
        for row in playerBoard:
            self.player_board.append([])
            for col in row:
                if col is not None:
                    self.player_board[-1].append("O")
                else:
                    self.player_board[-1].append(None)

        self.player_board = playerBoard
