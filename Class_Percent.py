class Student:
    def __init__(self,marks):
        self.marks=marks
    def per(self):
        return (self.marks/600)*100
    
s=Student(400)
print(s.marks)
print(s.per(),"%")
