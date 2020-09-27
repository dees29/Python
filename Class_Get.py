class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def msg(self):
        print(self.name+ " got " +self.marks,"%")

    @classmethod
    def get_per(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))
    @staticmethod
    def get_age(age):
        if age<17:
            print("belongs to school!!")
        else:
            print("don't belongs to school")
    
s1=Student("nia","93")
s2=Student.get_per("ria","400")
s2.msg()
s1.get_age(16)
