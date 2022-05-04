import json
import socket
from logging import getLogger

import models


class Scanner:
    logger = getLogger("scanner")
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
