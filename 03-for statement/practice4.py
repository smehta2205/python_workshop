s=input("Enter a string.")
flag=0
for i in range(len(s)):
  flag=1
  if(s[i]==s[len(s)-i-1]):
      flag=0
if(flag==0):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
