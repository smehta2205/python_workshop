try:
  x = float(input("Your number:"))
  inverse = 1.0/x
  print(inverse)

except ValueError:
    print("You should have given either an integer or a float.")

except ZeroDivisionError:
  print("Infinity!")

finally:
  print("There may or may not be an exception.")
