def fact(n):
    '''while(n>0)
        prod=n*fact(n-1)
    print(prod)'''
    if n==0:
        return 1
    else:
        ans=n*fact(n-1)
        return ans


a=int(input("Enter the number whose factorial is required."))
ans=fact(a)
print(ans)
