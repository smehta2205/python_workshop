fact=1
n=int(input("Enter a number whose factorial is needed."))
for i in range(1,n+1):
  fact=fact*i
print("Factorial={}".format(fact))
