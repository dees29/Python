def function1():
    print("hi i am function1")

def function2(func):
    print("hi i am function 2 now i'll call function1")
    func()

function2(function1)
