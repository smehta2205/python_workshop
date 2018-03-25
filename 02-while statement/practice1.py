x=0
while x<10:
    #print("----{}".format(x))
    if x%2==0:
        print(x)
    elif x%3==0:
        print("{} is multiple of 3".format(x))
    elif x%17==0:
        break
    x += 1
else:
    print("Puru")
