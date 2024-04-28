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
    def __init__(self, duration, start_date, course_title, student_names=[]):
        self.duration = duration
        self.start_date = start_date
        self.course_title = course_title
        self.student_names = student_names

    def Create_Contract(self):
        for student in self.student_names:
            print(f"Contarct for {student} is created with start_date - {self.start_date} and duration {self.duration} month")
    
              
    def Certification(self):
        for student in self.student_names:
             print(f"Certificate is presented to {student} for finishing {self.course_title} course")
        



class Automated_Testing(Courses):
    def __init__(self, duration, start_date, course_title, student_names):
        super().__init__(duration, start_date, course_title, student_names)


    def Learn_Python(self):
        return "Python Agenda"
    
    def Learn_Selenium(self):
        return "Selenium Agenda"
    


new_instance = Automated_Testing("4", "26.02.2024", "Automated Testing", student_names=["Arman", "Anna", "Lusine"])
print(new_instance.Create_Contract())
print(new_instance.Learn_Python())
print(new_instance.Learn_Selenium())
print(new_instance.Certification())
    
