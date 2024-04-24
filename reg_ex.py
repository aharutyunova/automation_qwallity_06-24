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



