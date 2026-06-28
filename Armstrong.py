n=153
temp=n
length=len(str(n))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**length
    n=n//10
if temp==sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")