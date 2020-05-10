class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def msg(self):
        print(self.name+ " got " +self.marks,"%")

    @classmethod
    def get_per(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))
    
s1=Student("nia","93")
marks="560"
name="nia"
s2=Student.get_per(name,marks)
s2.msg()
