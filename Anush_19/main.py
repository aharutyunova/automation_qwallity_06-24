import pymysql
import json

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

cursor = connection.cursor()

query = "SELECT * FROM courses"
cursor.execute(query)

course_data = cursor.fetchall()

advanced_courses = [{"id": row[0], "title": row[1]} for row in course_data]


def get_course_info(index):
    if 0 <= index < len(advanced_courses):
        return advanced_courses[index]["id"], advanced_courses[index]["title"]
    else:
        return None


def get_ten_courses():
    course_count = min(10, len(advanced_courses))
    ten_courses = []
    for i in range(course_count):
        ten_courses.append(get_course_info(i))
    return ten_courses


courses = get_ten_courses()
for course_id, course_title in courses:
    print(f"Course ID: {course_id}, Course Title: {course_title}")  
with open("validated_courses.json", "w") as f:
    json.dump(get_ten_courses(), f, indent=4)