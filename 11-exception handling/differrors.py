d={}
l=[]
filename = "C:\python"

try:
  print("Trying to be a math wiz...")
  print(1/1)

  d["key"]="value"
  print("Trying to access an inexistant key!")
  print(d["key"])

  f = open(filename)

except ZeroDivisionError:
    print("Math Error!!!")

except KeyError:
  print("Exception!!! The key does not exist!")

except:
    print("Exception hui gava!")
