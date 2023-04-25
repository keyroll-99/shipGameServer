from Endpoints.BaseController import BaseController
from Store.GameStore import GameStore
from Store.PlayerStore import PlayerStore


class GameRoomsController(BaseController):
    basePath = "game-room"
    actions = {}

    def __init__(self):
        self.actions = {
            "get-all": self.get_all,
            "create": self.create_room,
        }

    @staticmethod
    def get_all():
        filtered_list = list(filter(lambda x: x.can_other_player_join(), GameStore.games))
        return list(map(lambda x: x.name, filtered_list))

    @staticmethod
    def create_room(request):
        player = PlayerStore.find_by_name(request["playerName"])
        if GameStore.exists_by_name(request["name"]):
            return {"isSuccess": False, "message": "Room with this name exits"}
        GameStore.add_game(request["name"], player)
        return {"isSuccess": True}
