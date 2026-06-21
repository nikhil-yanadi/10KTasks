val=input()
d=0
n=len(val)-1
for i in range(len(val)):
    d+=int(val[i])*(2**(n-i))
print(d)