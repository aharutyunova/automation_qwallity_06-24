import log_in
import add_course
import get_fundamental_course
import update_course
import delete_course
from configs import username, password


def main():

    token = log_in.user_login(username, password)
    '''
    # Add course
    course_details = {
        "author": "Iza",
        "body": "something",
        "coursetype": "1",
        "price": 1500,
        "title": "Test_Iza"
    }
    add_course_response = add_course.add_course(course_details, token)
    print("Course added:", add_course_response)
    '''
    # Get Fundamental Course
    fundamental_course = get_fundamental_course.get_fundamental_course(token)
    print("Fundamental Course:", fundamental_course)

    # Update Course
    updated_course_details = {
        "author": "Iza_updated",
        "body": "something_updated",
    }
    course = add_course.add_course(updated_course_details, token)
    course_result = course.get("result", [])
    for i in course_result:
    update_course_response = update_course.update_course(course_id, updated_course_details, token)
    print("Updated Course:", update_course_response)
    '''
    # Delete Course
    delete_course_response = delete_course.delete_course(course_id, token)
    print("Delete Course:", delete_course_response)
    '''

if __name__ == "__main__":
    main()
