import sys
file_name = sys.argv[1]
text = []

try:
  fh = open(file_name, 'r')

except IOError:
  print("Cannot open", file_name)

else:
  text = fh.readlines()
  fh.close()
  print(text)
