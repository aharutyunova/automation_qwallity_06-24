"""
- Create parent Courses class with parameters
    duration, start_date, student_names, course_title
- Courses class should have following methods.

1.create_contract, which will print for each student
contarct for {student_name} is created witih start_date - {date} and duration {months} month

2.give_certificate which will print for each student
Certificate is presented to {student_name} for finishing {course_title} course

- Create Child class Automated_Testing which will have same parameters as parent class and 2 methods
1. learn_python, which will print 2 words "Python Agenda"
2. learn_selenium, which will print "Selenium Agenda"

- Create object of Automated_Testing, pass duration, start date, student list and course title
- Call object's methods in order, you get something like

contarct for Lusine is created witih start_date - 26.02.2024 and duration 4 month
contarct for Arman is created witih start_date - 26.02.2024 and duration 4 month
contarct for Anna is created witih start_date - 26.02.2024 and duration 4 month
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
        self.student_names = student_names.split(", ")
        self.course_title = course_title

    def create_contract(self):
        for student_name in self.student_names:
            print(f"contarct for {student_name} is created witih start date - {self.start_date} and duration {self.duration} month")

    def give_certificate(self):
        for student_name in self.student_names:
            print(f"Certificate is presented to {student_name} for finishing {self.course_title} course")


class Automated_Testing(Courses):
    def learn_python(self):
        print("Python Agenda")

    def learn_selenium(self):
        print("Selenium Agenda")


new_course_duration = 4
new_studendts_names = "Lusine, Arman, Anna"
new_course_start_date = "26.02.2024"
new_course_name = "Automated Testing"

new_course = Automated_Testing(new_course_duration, new_course_start_date, new_studendts_names, new_course_name)

new_course.create_contract()
new_course.give_certificate()

# Anna - exactly what I expect :)
# You only firget to call learn python and selenium before contract and certificate.
# So in your flow learning months are skipped :)
