import logging
import config

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=config.log_file_path,
        filemode='w+',
        encoding='utf-8'
    )

