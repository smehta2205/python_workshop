x=5
def func():
    global x
    print("Global x is {}".format(x))
    x=20
    print(x)
func()
print(x)
