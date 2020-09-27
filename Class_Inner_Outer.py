def outer(expr):
    def upper_d(func):
        def inner():
            return func()+expr
        return inner
    return upper_d


@outer("deepu")
def ordinary():
    return "good morning "

print(ordinary())
