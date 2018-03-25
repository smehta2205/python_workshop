a=int(input("Enter the value of one side of a triangle."))
b=int(input("Enter the value of 2nd side of a triangle."))
c=int(input("Enter the value of 3rd side of a triangle."))
if(a*a+b*b==c*c):
  print('The triangle is right angled triangle')
elif(a*a+c*c==b*b):
  print("The triangle is right angled triangle.")
elif(b*b+c*c==a*a):
  print("The triangle is right angled triangle.")
else:
  print("The triangle is not right angled triangle.")
