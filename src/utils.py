import logging


def create_logger() -> logging.Logger:

    logger = logging.getLogger()

    handler = logging.StreamHandler()
    logger.addHandler(handler)

    logger.setLevel(logging.INFO)

    return logger
