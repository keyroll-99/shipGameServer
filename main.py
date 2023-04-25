from App import App
from Endpoints.GameRoomsController import GameRoomsController
from Endpoints.PlayerController import PlayerController
from Endpoints.GameController import GameController

app = App()\
    .map_controller(GameRoomsController())\
    .map_controller(PlayerController())\
    .map_controller(GameController())

try:
    app.run()

finally:
    app.close()
