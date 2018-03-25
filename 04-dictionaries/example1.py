d1 = {
"amit":"amit@example.com",
"vijay":"vijay@example.com",
"ajay":"ajay@example.com"
}

d2={
1:"python",
2:"django",
3:"golang"
}

print(d1)
print(d2)

d1["singh"]="singh@example.com"
print(d1)
del d1["vijay"]
print(d1)

del d2[3]
print(d2)

#for multiple values to a single key, put all the values in a square brackets.
d2[4]="C++"
print(d2)

'''for i in d1:
    print(i,"-->",d1[i])'''
for i in d1.items():
        print(i)
#tuple is the type of the outputs whem the above statement is executed.
for k,v in d1.items():
    print(k,"-->",v)

print(d1.keys())
print(d1.values())

for i in d1.keys():
    print(i)
