import json
import re

# Read the text from text.txt file
with open("text.txt", "r") as file:
    text = file.read()

# Define a regular expression pattern to match the desired text format
pattern = r"(\d+)\s*:\s*(.*?)\s*Known song by (.*?)\s*$"

# Use the re.findall() method to find all matches of the pattern in the text
matches = re.findall(pattern, text, re.MULTILINE)

# Initialize an empty list to store the extracted data
result = []

# Initialize an empty dictionary to store the current match data
data = {}

# Iterate over each match found
for match in matches:
    # Extract the user ID, title, and body from the match
    user_id = int(match[0])
    title = match[1]
    body = match[2]

    # Create a dictionary representing the current match
    data = {
        "userId": user_id,
        "title": title,
        "body": body
    }

    # Append the current match data to the result list
    result.append(data)

# Print the JSON representation of the last match (optional, you may want to print result instead)
print(json.dumps(data, indent=4))
