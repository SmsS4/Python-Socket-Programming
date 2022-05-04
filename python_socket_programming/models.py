from enum import Enum


class MessageTypes(Enum):
    ABSTRACT = 1
    HELLO = 2


class AbstractModel:
    MESSAGE_TYPE = MessageTypes.ABSTRACT

    def __init__(self):
        self.message_type = self.MESSAGE_TYPE


class Hello(AbstractModel):
    MESSAGE_TYPE = MessageTypes.HELLO

    def __init__(self):
        super().__init__()


all_models = [
    AbstractModel, Hello
]
all_models_map = {
    model.MESSAGE_TYPE: model for model in all_models
}
