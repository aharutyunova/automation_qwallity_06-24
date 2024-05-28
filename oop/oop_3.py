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
    def __init__(self, duration, start_date, student_names, course_title ):
        self.duration = duration
        self.start_date = start_date
        self.student_names = student_names
        self.course_title = course_title


    def create_contract(self):
        for student_name in self.student_names:
            print(f"contarct for {self.student_names} is created witih {self.start_date} and {self.duration} month\n")
        
    def give_certificate(self):
        for course_title in self.course_title:
            print(f"Certificate is presented to {self.student_name} for finishing {self.course_title} course")


class Automated_Testing(Courses):
        def __init__(self, duration, start_date, student_names, course_title ):
            Courses().__init__(self, duration, start_date, student_names, course_title)


        def learn_python(self):
        print("Python Agenda")

        def learn_selenium(self):
        print("Selenium Agenda")


certificate = Automated_Testing(duration=4, start_date="26.02.2024", student_names=["Student 1", "Student 2", "Student 3"], course_title="Automated Testing")

certificate.create_contract()
certificate.learn_python()
certificate.learn_selenium()
certificate.give_certificate()