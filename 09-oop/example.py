class MyClass(object):
    var = 0
    def __init__(self):
        MyClass.var += 1

a = MyClass()
print(a.var)
b = MyClass()
print(b.var)
c = MyClass()
print(c.var)

MyClass.var +=1
print (a.var, b.var, c.var)
