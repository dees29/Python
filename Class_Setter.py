class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    
    def msg(self):
        return  self.name + " got grade " + self.grade
    def setter(self,msg):
        sent=msg.split(" ")
        print(sent)
        self.name=sent[0]
        self.grade=sent[-1]


    
stud1=Student("nia","B")
stud1.setter("deepu got grade A")
#stud1.msg="deepu got grade A"
print("name:",stud1.name)
print("grade:",stud1.grade)
print(stud1.msg)
