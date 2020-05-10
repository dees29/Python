class Student:
    counter=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.counter=Student.counter+1
    def msg(self):
        print(self.name+ " got " +self.marks,"%")

    @classmethod
    def object_count(cls):
        return cls.counter
    
s1=Student("nia","93")
s2=Student("ria","67")
s3=Student("sia","67")
print(Student.object_count())
print(s1.object_count())
