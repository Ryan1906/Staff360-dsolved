import logging
import sys

def setup_logger(name=__name__):

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # file_handler = logging.FileHandler("")
    # file_handler.setLevel(logging.INFO)
    # file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)
        # logger.addHandler(file_handler)

    return logger