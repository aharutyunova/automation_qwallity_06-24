import re
import logging

# 1. option without logging

text = """ # This is a comment
Width = 4 # box width
   Height = 3
Length = 6 """

pattern = r'(Width|Height|Length)\s*=\s*(\d+)'
result = re.findall(pattern, text)
print(dict(result))


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

# Anna - The solution is working and data extract and convert way optimal enough
# For using logging you should have defined basicConfig, like this
"""

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='my_log.log',
    filemode='w+',
    encoding='utf-8'
)
"""

