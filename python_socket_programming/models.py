from enum import IntEnum
from typing import Optional


class MessageTypes(IntEnum):
    ABSTRACT = 1
    HELLO = 2


class AbstractModel:
    MESSAGE_TYPE = MessageTypes.ABSTRACT

    def __init__(self, message_type: Optional[MessageTypes]):
        if message_type:
            self.message_type = message_type
        else:
            self.message_type = self.MESSAGE_TYPE


class Hello(AbstractModel):
    MESSAGE_TYPE = MessageTypes.HELLO

    def __init__(self, message_type: MessageTypes = MessageTypes.HELLO):
        super().__init__(message_type)


all_models = [
    AbstractModel, Hello
]
all_models_map = {
    model.MESSAGE_TYPE: model for model in all_models
}
