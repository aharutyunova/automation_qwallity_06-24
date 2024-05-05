import re
import logging
from BaseException import BaseException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='phone_number_check.log',
    filemode='w+',
    encoding='utf-8'
)

# Define the phone numbers to check
phone_numbers = [
    "+1-123-456-7890",
    "+1234567890",
    "+123-456-7890",
    "1234567890",
    "+374333399",  # AMR
    "123-456-7890",
    "123",
    "+12A-345-6789",  # Invalid: contains non-numeric characters
    "+123-456-78901234567890"  # Invalid: too many digits
]

# Define the regex pattern for phone numbers
pattern = r'^\+?\d{1,3}-?\d{3,14}$'

# Create a logger
logger = logging.getLogger(__name__)

# Loop through each phone number and check it against the regex pattern
for phone_number in phone_numbers:
    if re.match(pattern, phone_number):
        logger.info(f"{phone_number}: Valid phone number")
    else:
        logger.warning(f"{phone_number}: Invalid phone number")

# Log a message indicating the end of the phone number checking process
logger.info("Phone number checking complete.")