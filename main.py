from App import App
from Endpoints.GameRoomsController import GameRoomsController
from Endpoints.PlayerController import PlayerController

app = App()\
    .map_controller(GameRoomsController())\
    .map_controller(PlayerController())

try:
    app.run()

finally:
    app.close()
