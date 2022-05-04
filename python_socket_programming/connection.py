import json
import socket

import models
from python_socket_programming.logger import get_logger


class Connection:
    logger = get_logger("connection")
    DELIMITER = '$'

    def __init__(self, connection: socket.socket):
        self.connection = connection
        self.buffer = ''

    def parse(self, message: str) -> models.AbstractModel:
        message = json.loads(message)
        return models.all_models_map[message['message_type']](**message)

    def next_token(self) -> models.AbstractModel:
        if self.DELIMITER not in self.buffer:
            self.buffer += self.connection.recv(1024).decode()
        pos = self.buffer.find(self.DELIMITER)
        message = self.parse(self.buffer[:pos])
        self.buffer = self.buffer[pos + 1:]
        self.logger.info("New message %s", message.message_type)
        return message

    def send_message(self, message: models.AbstractModel):
        self.logger.info("Sending new message %s", message.message_type)
        self.connection.send(
            (json.dumps(message, default=lambda x: x.__dict__) + self.DELIMITER).encode()
        )
