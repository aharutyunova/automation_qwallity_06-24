import logging
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(CURRENT_DIR, 'log_file_28.log')


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(filename)s:'
        '%(lineno)d - %(funcName)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=log_file_path,
        filemode='w+',
        encoding='utf-8'
    )


url = "https://qwallity-prod.onrender.com"