from database import DB

# Create an instance of the DB class
db = DB(host='pro.freedb.tech', user='qwallity', password='6YJsZQk&##7J2?e', database='qwallitydb')

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


# Anna - General structure is correct, still I have some questions
# Why in update method you return 3? is it hardcoded value of updated rows? You should get it via cursor.rowcount 
# and check if cursor.rowcount == 3 then commit your update in othercase rollback

# Your example with test data localhost, username, password... did you try execute with our db dredentials?

# And one note in case you get cursor in init method, then db_connection method is additonal