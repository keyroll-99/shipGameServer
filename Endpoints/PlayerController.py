from Endpoints.BaseController import BaseController
from Models.Player import Player
from Store.PlayerStore import PlayerStore
from Store.GameStore import GameStore

class PlayerController(BaseController):
    basePath = "player"
    actions = {}

    def __init__(self):
        self.actions = {
            "join": self.join_to_server,
            "exit": self.exit,
        }

    @staticmethod
    def join_to_server(playerName):
        player_exits = len(list(filter(lambda x: x.name == playerName, PlayerStore.players))) > 0
        if player_exits:
            return {"isSuccess": False, "message": "Player with this name exits"}

        PlayerStore.players.append(Player(playerName))
        return {"isSuccess": True}

    @staticmethod
    def exit(playerName):
        GameStore.remove_all_player_game(playerName)
        PlayerStore.remove_player(playerName)
        return {"isSuccess": True}
