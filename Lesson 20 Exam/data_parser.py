import re


def parse_text(line):
    line = re.sub(r'#.*', '', line)
    parts = re.split(r'\t|:', line)
    parts = [part.strip() for part in parts]
    if len(parts) >= 3:
        user_id, title, body = parts[:3]
        return {"userId": int(user_id), "title": title, "body": body}
    else:
        return None


def parse_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                parsed_line = parse_text(line)
                if parsed_line:
                    data.append(parsed_line)
    return data
