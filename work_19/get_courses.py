import requests
from jsonschema import validate

from endpoints import FUNDAMENTAL_COURSE_ENDPOINT

# Define the schema for course data validation
course_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"}
    },
    "required": ["id", "title"]
}

def get_advanced_courses():
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(FUNDAMENTAL_COURSE_ENDPOINT, headers=headers)
        response.raise_for_status()
        advanced_courses = response.json()
        
        # Validate the response data against the schema
        for course in advanced_courses:
            validate(instance=course, schema=course_schema)

        # Extract 10 unique course IDs and titles
        limited_courses = []
        seen_ids = set()
        for course in advanced_courses:
            if len(limited_courses) == 10:
                break
            course_id = course.get("id")
            course_title = course.get("title")
            if course_id and course_title and course_id not in seen_ids:
                limited_courses.append({"id": course_id, "title": course_title})
                seen_ids.add(course_id)

        return limited_courses
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        if response.status_code == 401:
            print("Unauthorized: Check your credentials.")
        return None

# Example usage:
advanced_courses = get_advanced_courses()
if advanced_courses:
    for course in advanced_courses:
        print(f"ID: {course['id']}, Title: {course['title']}")
else:
    print("Failed to retrieve advanced courses.")
