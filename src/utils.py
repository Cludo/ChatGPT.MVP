import logging


def create_logger() -> logging.Logger:
    """
    Create a logger object.

    :return: a logger object
    """
    logger = logging.getLogger()

    handler = logging.StreamHandler()
    logger.addHandler(handler)

    logger.setLevel(logging.INFO)

    return logger
