while True:
  try:
      n=int(input("Enter an integer."))
      #n=int(n)
      break
  except ValueError:             #type of exception need not be specified.
    print("No valid integer! Please try again...")

print("Great, you have successfully entered an integer!")
