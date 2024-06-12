import logging

def logging_():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='loggingInfo.log', 
                    filemode='w+', 
                    encoding='utf-8')
    print("Logging configuration applied")