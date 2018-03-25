import sys

try:
  f = open("integers.txt")
  s = f.readline()
  i = int(s.strip())

except IOError as err:
  print("I/O Error(%d) : %s"%(err.errno, err.strerror))
  print(dir(err))

except ValueError:
  print("No valid integers in line.")

except:
  print("Unexcepted error:",sys.exc_info()[0])
