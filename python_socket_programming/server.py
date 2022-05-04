import socket
import threading

from python_socket_programming import SERVER_PORT, models
from python_socket_programming.connection import Connection
from python_socket_programming.logger import get_logger


class Server:
    logger = get_logger("server")

    def __init__(self, port: int):
        self.port = port

    def handle_socket(self, connection: socket.socket):
        connection = Connection(connection)
        while True:
            token = connection.next_token()
            self.logger.info("new token %s", token)
            connection.send_message(models.Hello())

    def start(self):
        self.logger.info("Starting server")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("localhost", self.port))
            s.listen()
            while True:
                connection, address = s.accept()
                self.logger.info("New socket connection by %s", address)
                threading.Thread(target=self.handle_socket, args=(connection,)).start()


def main():
    server = Server(SERVER_PORT)
    server.start()


if __name__ == "__main__":
    main()
