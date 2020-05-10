class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        self.msg=self.name + " got grade " + self.grade

    
stud1=Student("nia","B")
stud1.grade="A"
print("name:",stud1.name)
print("grade:",stud1.grade)
print(stud1.msg)
