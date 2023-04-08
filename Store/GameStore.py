from Models.Game import Game, Player


class GameStore:
    games: list[Game] = []

    @staticmethod
    def add_game(name: str, player: Player):
        GameStore.games.append(Game(name, player))

    @staticmethod
    def get_all() -> list[Game]:
        return GameStore.games
