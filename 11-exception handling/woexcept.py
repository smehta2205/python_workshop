import sys
file_name = sys.argv[1]
text = []

try:
  fh = open(file_name, 'r')
  text = fh.readlines()
  fh.close()

except IOError:
  print("Cannot open", file_name)

if text:
  print(text)
