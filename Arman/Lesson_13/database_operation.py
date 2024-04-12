from database import DB

# Create an instance of the DB class
db = DB(host='localhost', user='username', password='password', database='database')

# Update three courses
courses_to_update = [
    (1, 'course_1'),
    (2, 'Course_2'),
    (3, 'Course_3')
]

for course_id, new_title in courses_to_update:
    result = db.update(course_id, new_title)
    if result == 3:
        print(f"Course with ID {course_id} updated successfully.")
    else:
        print(f"Failed to update course with ID {course_id}. Error: {result}")

# Close the database connection
db.db_close()
