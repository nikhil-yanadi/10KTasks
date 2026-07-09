def add(a,b):
    return a+b
def square(n):
    return n*n
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def maximum(a, b):
    return a if a>b else b

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def count_vowels(s):
    count=0
    for ch in s:
        if ch in "aeiouAEIOU":
            count+=1
    return count
def reverse_string(s):
    return s[::-1]
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True
def list_sum(lst):
    total=0
    for i in lst:
        total+=i
    return total
def palindrome(s):
    return "Palindrome" if s == s[::-1] else "Not Palindrome"
print("Addition:", add(10, 20))
print("Square:", square(7))
print("Even/Odd:", even_odd(15))
print("Maximum:", maximum(25, 40))
print("Factorial:", factorial(5))
print("Vowel Count:", count_vowels("Python Programming"))
print("Reverse:", reverse_string("Python"))
print("Prime:", is_prime(17))
print("List Sum:", list_sum([10, 20, 30, 40]))
print("Palindrome:", palindrome("madam"))
