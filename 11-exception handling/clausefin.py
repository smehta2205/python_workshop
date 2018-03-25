inverse = None
try:
  x = float(input("Your number:"))
  inverse = 1.0/x

except:
    print("You cannot divide a number by 0!")

finally:
  print("There may or may not be an exception.")

print("The inverse is: " , inverse)
