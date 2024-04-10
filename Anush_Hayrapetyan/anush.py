class Courses:
    def __init__(self, duration, start_date, student_name, course_title):
        self.duration = duration
        self.start_date = start_date
        self.student_name = student_name
        self.course_tittle = course_title

    def create_contract(self):
        pass

    def give_sertificate(self):
        pass


class Anuthomation(Courses):
    def learn_p(self):
        print("Python Agenda")

    def learn_s(self):
        print("Selenium Agenda")


main_course = Anuthomation(
    duration=5,
    start_date="15.04",
    student_name=["Anush, Anna"],
    course_title="Auth_testing"
)


main_course.create_contract()