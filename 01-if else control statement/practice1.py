a=int(input("Enter a number"))
b=int(input("Enter another number"))
c=input("Enter your choice.+.Addition  -.Subtraction  *.Multiplication  /.Division")
if c == '+':
  print("Your choice is +")
  print('Result={}+{}={}'.format(a,b,a+b))
elif c == '-':
  print("Your choice is -")
  print('Result={}-{}={}'.format(a,b,a-b))
elif c == '*':
  print("Your choice is *")
  print('Result={}*{}={}'.format(a,b,a*b))
else:
  print("Your Choice is /")
  print('Result={}/{}={}'.format(a,b,a/b))
