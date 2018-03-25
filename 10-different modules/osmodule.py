import os
print(os.getcwd())
print("Moving to parent directory.")
os.chdir(os.pardir)
print(os.getcwd())
#print(os.getuid())
print(os.environ)
#print(os.getgid())

print(os.path.exists("\ "))
print(os.path.isdir("\ "))
print(os.path.isdir("\osmodule "))
print(os.path.isdir("\python workshop "))

for i in os.walk(os.getcwd()):
    print(i)
