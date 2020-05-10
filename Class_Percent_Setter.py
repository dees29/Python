class Student:
    def __init__(self,marks):
        self.__marks=marks
    def per(self):
        return (self.__marks/600)*100
    def setter(self,value):
        self.__marks=value
    def getter(self):
        return self.__marks 
    
s=Student(400)
#s.marks=500
s.setter(500)
print(s.getter())
#print(s.marks)
print(s.per(),"%")
