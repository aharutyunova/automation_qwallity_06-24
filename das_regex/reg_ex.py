import re
import logging from BaseException

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='phone_number_check.log',
    filemode='w+',
    encoding='utf-8'
)

# Log a message
logging.info("Logging started.")

# Example without logging
text = """ # This is a comment
Width = 4 # box width
   Height = 3
Length = 6 """

pattern = r'(Width|Height|Length)\s*=\s*(\d+)'
result = re.findall(pattern, text)
print(dict(result))

# Log a message
logging.info("Processing complete.")


# 2. with logging

text = """ # This is a comment
Width = 4 # box width
   Height = 3
Length = 6 """

pattern = r'(Width|Height|Length)\s*=\s*(\d+)'


result = re.findall(pattern, text)

try:
    result = result

except BaseException as e:
    logging.error(e)

finally:
    print(dict(result))


# 3. regex_check phone number 
import re
import logging

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


# 4. email address

import os
import re
import logging

def is_valid_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        logging.info(f"Valid email address: {email}")
        return True
    else:
        logging.warning(f"Invalid email address: {email}")
        return False

# Test the function with some example email addresses
emails = [
    "user@example.com",
    "user123@gmail.com",
    "user.name@example.com",
    "user123@example",
    "user@123.com",
    "user@example..com",
    "user@.example.com",
    "user@example_com",
    "user@example.c",
    "@example.com",
    "user",
]

# Configure logging
log_dir = "logs"
log_file = os.path.join(log_dir, "email_validation.log")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
with open(log_file, 'w+') as f:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(f),
            logging.FileHandler(log_file)
        ]
    )

    for email in emails:
        print(f"{email}: {is_valid_email(email)}")
