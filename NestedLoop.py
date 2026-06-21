# Sum of Digits
n=1234
sum=0
while n>0:
    sum+=n%10
    n//=10
print(sum)

# Reverse a number
n=1234
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)

# Count digits in a number
n=12345
cnt=0
while n>0:
    cnt+=1
    n//=10
print(cnt)

# Check even or odd
n=17
if n%2==0:
    print("Even")
else:
    print("Odd")

# Check prime number
n=13
p=0
for i in range(2,n):
 if n%i==0:
  p=1
  break
if n>1 and p==0:
   print("Prime")
else:
   print("Not Prime")

#Find factorial
n=5
fact=1
for i in range(1,n+1):
 fact*=i
print(fact)

#Find factors
n=12
for i in range(1,n+1):
 if n%i==0:
  print(i,end=" ")
print()

#Check palindrome or not 
n=121
temp=n
rev=0
while n>0:
 rev=rev*10+n%10
 n//=10
if temp==rev:
  print("Palindrome")
else:
  print("Not palindorme")

#Find armstrong number
n=153
temp=n
st=0
while n>0:
 d=n%10
 st+=d**3
 n//=10
if temp==st:
  print("Armstrong")
else:
  print("Not Armstrong")

#GCD and HCF of number
a,b=12,18
while b:
 a,b=b,a%b
print(a)
