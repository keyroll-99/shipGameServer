from Endpoints.BaseController import BaseController
from Store.GameStore import GameStore
from Store.PlayerStore import PlayerStore


class GameRoomsController(BaseController):
    basePath = "game-room"
    actions = {}

    def __init__(self):
        self.actions = {
            "get-all": self.get_all,
            "add": self.add_game
        }

    @staticmethod
    def get_all():
        return list(map(lambda x: x.name, GameStore.games))

    @staticmethod
    def add_game(request):
        player = PlayerStore.find_by_name(request["playerName"])
        GameStore.add_game(request["name"], player)
        return {"isSuccess": True}
