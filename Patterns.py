n=5
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
print()

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
print()

for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
print()

for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
print()

m=65
for i in range(n):
    for j in range(i+1):
        print(chr(m+j),end=" ")
    print()
print()

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

m=1
for i in range(n):
    for j in range(i+1):
        print(m,end=" ")
        m+=1
    print()
print()

for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
print()

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()