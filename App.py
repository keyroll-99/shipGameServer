import json

from Endpoints.BaseController import BaseController
import socket
import Config


class App:
    sock: socket.socket
    endpoints = {}

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def map_controller(self, controller: BaseController):
        if controller.basePath in self.endpoints.keys():
            raise Exception("Multiple endpoints with same path")

        self.endpoints[controller.basePath] = controller

        return self

    def run(self):
        self.sock.bind((Config.HOST_NAME, Config.SERVER_PORT))
        self.sock.listen(6)
        while True:
            conn, addr = self.sock.accept()
            with conn:
                request = conn.recv(1024)
                try:
                    data = json.loads(request.decode("utf-8"))
                    action = data["action"]
                    controller = action['controller']
                    action = action['route']
                    response = {}
                    if "data" in data.keys():
                        response = self.endpoints[controller].actions[action](data["data"])
                    else:
                        response = self.endpoints[controller].actions[action]()
                    conn.send(bytes(f'{json.dumps(response)}', "utf-8"))
                except Exception as e:
                    print(e)
                    error_response = {"message": "server-error"}
                    conn.send(bytes(f"{json.dumps(error_response)}", "utf-8"))

    def close(self):
        self.sock.close()

    def call_endpoint(self, endpoint, data):
        if endpoint not in self.endpoints.keys():
            return {"isSuccess": False, "Message": "endpoint doesnt exits"}

        if data is not None:
            return self.endpoints[endpoint]
        return self.endpoints[endpoint]()
