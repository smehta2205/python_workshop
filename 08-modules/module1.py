#sysmodules
def addition(a, b):
  return a+b

def ask_for_integers():
  a=int(input("Enter first integer."))
  b=int(input("Enter second integer."))
  return a , b

if __name__=="__main__":
        x, y=ask_for_integers()
        n=addition(x,y)
        print(n)
'''else:
    print("Being used as a module!")'''
