from Endpoints.BaseController import BaseController
from Store.GameStore import GameStore
from Store.PlayerStore import PlayerStore


class GameController(BaseController):
    basePath = "game"
    actions = {}

    def __init__(self):
        self.actions = {
            "join": self.join_to_game,
            "can-start": self.can_game_start,
            "get-game-data": self.get_game_data,
            "ready": self.ready
        }

    @staticmethod
    def join_to_game(request):
        player_name = request["playerName"]
        game_name = request["gameName"]
        game = GameStore.find_by_name(game_name)
        player = PlayerStore.find_by_name(player_name)

        if game is None or player is None:
            return {"isSuccess": False, "message": "invalid request"}

        if not game.can_other_player_join():
            return {'isSuccess': False, "message": "room is full"}

        game.join(player)
        return {'isSuccess': True}

    @staticmethod
    def can_game_start(request):
        game_name = request["name"]
        game = GameStore.find_by_name(game_name)
        can_other_player_join = game.can_other_player_join()
        can_start = not can_other_player_join
        return {"canStart": can_start}

    @staticmethod
    def get_game_data(request):
        game_name = request["gameName"]
        player_name = request["playerName"]
        game = GameStore.find_by_name(game_name)
        if game is None:
            return {"isSuccess": False}

        return game.get_game_data(player_name)

    @staticmethod
    def ready(request):
        player_name = request["playerName"]
        player_board = request["playerBoard"]
        gameName = request["gameName"]
        player = PlayerStore.find_by_name(player_name)
        player.set_is_ready(player_board)

        game = GameStore.find_by_name(gameName)
        game.set_game_phase()

        return {"isSuccess": True}

