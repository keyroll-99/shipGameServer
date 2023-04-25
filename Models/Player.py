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
        self.player_board = [[0] * 10 for _ in range(10)]
        self.player_hit = [[0] * 10 for _ in range(10)]
        self.ready = False
