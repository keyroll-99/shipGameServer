from Models.Game import Game, Player


class GameStore:
    games: list[Game] = []

    @staticmethod
    def add_game(name: str, player: Player):
        GameStore.games.append(Game(name, player))

    @staticmethod
    def get_all() -> list[Game]:
        return GameStore.games

    @staticmethod
    def find_by_name(name: str) -> Game | None:
        try:
            return list(filter(lambda x: x.name == name, GameStore.games))[0]
        except:
            return None

    @staticmethod
    def exists_by_name(name: str) -> bool:
        return len(list(filter(lambda x: x.name == name, GameStore.games))) > 0

    @staticmethod
    def remove_all_player_game(player_name: str):
        player_games = list(
            filter(lambda x: x.player1.name == player_name or x.player2 is None or x.player2.name == player_name,
                   GameStore.games))
        for player_game in player_games:
            player_game.close_game()

        GameStore.games = list(
            filter(lambda x: x.player1.name != player_name and (x.player2 is None or x.player2.name != player_name),
                   GameStore.games))
