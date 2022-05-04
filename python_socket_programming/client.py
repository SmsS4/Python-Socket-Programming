import socket

from python_socket_programming import SERVER_PORT, models
from python_socket_programming.connection import Connection
from python_socket_programming.logger import get_logger


class Client:
    logger = get_logger("client")

    def __init__(self, port: int):
        self.port = port
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect(("localhost", port))
        self.connection = Connection(connection)
        self.logger.info("Client connected")
        self.start()

    def start(self):
        self.connection.send_message(models.Hello())
        while True:
            token = self.connection.next_token()
            self.logger.info("New token %s", token.message_type)


def main():
    Client(SERVER_PORT)


if __name__ == "__main__":
    main()
