import logging


def configure_logging():
    logging.basicConfig(
        filename='my_log.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filemode='w+'
    )