#varArgs
def my_func(x,y=5,*args,**kwargs):      #keyword arguments
  print(x)
  print(y)
  print(args)
  print(kwargs)

#my_func(2,3,4,5,6,k=1,j='a')
#my_func(1,2,5,x=3,y=9,j=1,k=2)

d={'k':1,'j':9}
l=[11,12,13]
my_func(2,3,4,5,6,**d)
my_func(2,3,*l,**d)
my_func(2,3,*l,k=100,j=10000)
my_func(2,3,*[4,5,6],**d)
my_func(2,3,[4,5,6],**d)
