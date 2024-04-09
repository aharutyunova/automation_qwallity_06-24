"""
- Create parent Courses class with parameters
    duration, start_date, student_names, course_title

- Courses class should have the following methods.

1.create_contract, which will print for each student
contract for {student_name} is created with start_date - {date} and duration {months} month

2.give_certificate which will print for each student
Certificate is presented to {student_name} for finishing {course_title} course

- Create Child class Automated_Testing which will have same parameters as parent class and 2 methods
1. learn_python, which will print 2 words "Python Agenda"
2. learn_selenium, which will print "Selenium Agenda"

- Create object of Automated_Testing, pass duration, start date, student list and course title
- Call object's methods in order, you get something like

contract for Lusine is created with start_date - 26.02.2024 and duration 4-month
contract for Arman is created with start_date - 26.02.2024 and duration 4-month
contract for Anna is created with start_date - 26.02.2024 and duration 4-month
Python Agenda
Selenium Agenda
Certificate is presented to Lusine for finishing Automated testing course
Certificate is presented to Arman for finishing Automated testing course
Certificate is presented to Anna for finishing Automated testing course
"""


class Courses:

    def __init__(self, duration, start_date, student_names, course_title):
        self.duration = duration
        self.start_date = start_date
        self.student_names = student_names
        self.course_title = course_title

    def create_contract(self):
        """ Create contract method for student """
        return (f"Contract for {self.student_names} is created with start date"
                f" - {self.start_date} and duration {self.duration} month")

    def give_certificate(self):
        """ Give certificate method for user """
        return (f"Certificate is presented to {self.student_names}"
                f" for finishing {self.course_title} course")


class AutomatedTesting(Courses):

    @staticmethod
    def learn_python():
        return "Python Agenda"

    @staticmethod
    def learn_selenium():
        return "Selenium Agenda"


# Create instances for each student
student_1 = AutomatedTesting("4", "26.02.2024", "Lusine", "Python lesson")
student_2 = AutomatedTesting("4", "26.02.2024", "Arman", "Python lesson")
student_3 = AutomatedTesting("4", "26.02.2024", "Anna", "Python lesson")

# Create contract for student
print(student_1.create_contract())
print(student_2.create_contract())
print(student_3.create_contract())

# Student Python and Selenium courses
print(student_1.learn_python())
print(student_2.learn_selenium())

# Give certificate to student
print(student_1.give_certificate())
print(student_2.give_certificate())
print(student_3.give_certificate())
