def getinfo():
  nm=input("Enter the name.")
  rno=input("Enter the id number.")
  return nm, rno

def storage():
  f=open("C:\python workshop\ studentinfo","a")
  x, y=getinfo()
  f.write(x)
  f.write("\t")
  f.write(y)
  f.write("\n")
  f.close()
