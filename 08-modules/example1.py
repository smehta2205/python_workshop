#import os
#print(os.getcwd())

import sys
print("Arguments %s:"%sys.argv)
print("Path %s"%sys.path)
print(type(sys.path))
for i in sys.path:
    print(i)
