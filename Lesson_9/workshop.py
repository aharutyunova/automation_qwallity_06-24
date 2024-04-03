"""Write a class which will get Student name and score and have score checking
If score is more than 100 - print Dear <student name>, congratulations your score is high
otherwise print "Dear <student name>, your score is not enough

Create objects from that class, pass different names and score and check score message
"""
class Student:
    def __init__ (self, name, score):
        self.name = name
        self.score = score 
    def check_score(self):
        if self.score > 100:
            print(f'Dear {self.name}, congratulations your score is high')
        else:
            print(f'Dear {self.name}, your score is not enough')

student1 = Student("Anna", 98)
print(student1.name, student1.score)
student2 = Student("Hasmik", 101)
print(student2.name, student2.score)
student1.check_score()
student2.check_score()



     