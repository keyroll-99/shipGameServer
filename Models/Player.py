import socket


class Player:
    name: str = ""
    sock: socket

    def __init__(self, name):
        self.name = name
