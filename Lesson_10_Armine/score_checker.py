class Student:
    def __init__(self, name, score):
        self.name = name 
        self.score = score
           
    def my_func(self):
        if self.score > 100:
            print(f"Dear {self.name},congratulations yours score is high")
        else: 
            print(f"Dear {self.name},your score is not enough")


student_1 = Student("Alvard", 105)
student_1.my_func()

student_2 = Student("Poghos", 100)
student_2.my_func()
