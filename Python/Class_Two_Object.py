class Student:
    clg_name="xyz"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def msg(self):
        print(self.name+" "+self.age)
    
    
print("object 1:")
s1=Student("nia","20")
print(s1.name)
print(s1.age)
print(s1.clg_name)
s1.msg()
print("************")
print("object 2:")
s2=Student("ria","21")
print(s2.name)
print(s2.age)
print(s2.clg_name)
s2.msg()
