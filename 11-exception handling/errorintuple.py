try:
  f = open("integers.txt")
  s = f.readline()
  i = int(s.strip())
  print(i)

except(IOError, ValueError):
  print("An I/O error or Value error occured.")

except:
  print("An unexpected error occured.")
