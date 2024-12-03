import logging  # Import the logging module to enable logging of errors and other information

# Configure logging to a file
logging.basicConfig(filename='Log_file.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
