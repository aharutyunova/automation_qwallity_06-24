"""
- Create parent Courses class with parameters
    duration, start_date, student_names, course_title
- Courses class should have following methods.
1.create_contract, which will print for each student
contarct for {student_name} is created witih start_date - {date} and duration
{months} month
2.give_certificate which will print for each student
Certificate is presented to {student_name} for finishing {course_title} course

- Create Child class Automated_Testing which will have same parameters as
parent class and 2 methods
1. learn_python, which will print 2 words "Python Agenda"
2. learn_selenium, which will print "Selenium Agenda"
- Create object of Automated_Testing, pass duration, start date, student list
 and course title
- Call object's methods in order, you get something like

contarct for Lusine is created witih start_date - 26.02.2024 and duration 4
month
contarct for Arman is created witih start_date - 26.02.2024 and duration 4
 month
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
        self.student_names = student_names
        self.course_title = course_title

    def create_contract(self):
        print(f"Contarct for {self.student_names} is created witih start_date - {self.start_date} and duration {self.duration} month")

    def give_certificate(self):
        print(f"Certificate is presented to {self.student_names} for finishing {self.course_title} course")


class Automated_Testing(Courses):

    def learn_python(self):
        print("Python Agenda")

    def learn_selenium(self):
        print("Selenium Agenda")


obj1 = Automated_Testing("4", "26.02.2024", "Liana", "Automated testing")
obj2 = Automated_Testing("4", "26.02.2024", "Hamest", "Automated testing")
obj3 = Automated_Testing("4", "26.02.2024", "Lusine", "Automated testing")

obj1.create_contract()
obj2.create_contract()
obj3.create_contract()

obj1.learn_python()
obj1.learn_selenium()

obj1.give_certificate()
obj2.give_certificate()
obj3.give_certificate()

# Anna - the result is correct, but will be more effective if you pass not separate names, but list of names to your class
# And your create_contract and give_certificate methods using for loop would print same message for all studetns
# With this you could create one object for Automated_Testing class and call just once each method from that object