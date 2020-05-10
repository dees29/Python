class Student:
    def __init__(self,marks):
        self.__marks=marks
    def per(self):
        return (self.__marks/600)*100
    
    def getter(self):
        print("getting value:",end="")
        return self.__marks
    
    def setter(self,value):
        if value<0 or value>600:
            print("can't set the value stick to previous value")
        else:
            print("setting value:",value)
            self.__marks=value

    marks=property(getter,setter)
    
    
s=Student(400)
s.marks=599
print(s.marks)
print(s.per(),"%")
