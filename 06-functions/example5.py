#keyword arguments
def my_func(x,y=10,z=20):
  print(x,y,z)

my_func(y=1,x=5)
my_func(1,z=4,y=2)
my_func(y=2,z=4)    #error!!
