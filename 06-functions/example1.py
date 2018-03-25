def maximum(a,b):
  if a>b:
    print("{} is greater than {}".format(a,b))
  elif a<b:
    print("{} is greater than {}".format(b,a))
  else:
    print("{}={}".format(a,b))
a=int(input("Enter a number."))
b=int(input("Enter another number."))
maximum(a,b)
