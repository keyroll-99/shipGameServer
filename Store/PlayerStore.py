from Models.Player import Player


class PlayerStore:
    players: list[Player] = []

    @staticmethod
    def find_by_name(name: str) -> Player:
        players = list(filter(lambda x: x.name == name, PlayerStore.players))
        return players[0]

    @staticmethod
    def remove_player(name: str):
        PlayerStore.players = list(filter(lambda x: x.name != name, PlayerStore.players))
