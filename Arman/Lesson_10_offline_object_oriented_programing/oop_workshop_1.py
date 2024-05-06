"""
Write a class which will get Student name and score and have score checking

If score is more than 100 - print "Dear <student name>, congratulations your score is high"

otherwise print "Dear <student name>, your score is not enough"

Create objects from that class, pass different names and score and check score message
"""


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def check_student_score(self):
        if self.score > 100:
            return f"Dear {self.name}, congratulations your score is high"
        else:
            return f"Dear {self.name}, your score is not enough"


student_1 = Student("Arman", 101)
student_2 = Student("Suzanna", 109)
student_3 = Student("Anna", 102)
student_4 = Student("Diana", 90)
student_5 = Student("Adriana", 99)

print(student_1.check_student_score())
print(student_2.check_student_score())
print(student_3.check_student_score())
print(student_4.check_student_score())
print(student_5.check_student_score())
