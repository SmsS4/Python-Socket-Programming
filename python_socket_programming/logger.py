import logging
from logging import getLogger

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s::%(module)s::%(lineno)d | %(message)s",
    level=logging.DEBUG,
)


def get_logger(name: str) -> logging.Logger:
    return getLogger(name)
