# Write a program to find the area of a rectangle.
l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
area=l*b
print("Area is",area)

# Write a program to find the area of a square.
a=int(input("Enter the side: "))
area=a*a
print("Area is",area)

# Write a program to find the area of a triangle.
b=int(input("Enter the base: "))
h=int(input("Enter the height: "))
area=0.5*b*h
print("Area is",area)

# Write a program to find the area of a circle.
r=int(input("Enter the radius: "))
area=3.14*r*r
print("Area is",area)

# Write a program to find the area of a parallelogram.
b=int(input("Enter the base: "))
h=int(input("Enter the height: "))
area=b*h
print("Area is",area)

# Write a program to find the area of a rhombus.
d1=int(input("Enter diagonal 1: "))
d2=int(input("Enter diagonal 2: "))
area=0.5*d1*d2
print("Area is",area)

# Write a program to find the area of a trapezium.
a=int(input("Enter side a: "))
b=int(input("Enter side b: "))
h=int(input("Enter the height: "))
area=0.5*(a+b)*h
print("Area is",area)

# Write a program to find the area of an equilateral triangle.
a=int(input("Enter the side: "))
area=(1.732/4)*a*a
print("Area is",area)

# Write a program to find the area of a sector of a circle.
r=int(input("Enter the radius: "))
theta=int(input("Enter the angle: "))
area=(theta/360)*3.14*r*r
print("Area is",area)

# Write a program to find the area of a semicircle.
r=int(input("Enter the radius: "))
area=0.5*3.14*r*r
print("Area is",area)


print("PERIMETER PROBLEMS")
# Write a program to find the perimeter of a rectangle.
l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
perimeter=2*(l+b)
print("Perimeter is",perimeter)

# Write a program to find the perimeter of a square.
a=int(input("Enter the side: "))
perimeter=4*a
print("Perimeter is",perimeter)

# Write a program to find the circumference of a circle.
r=int(input("Enter the radius: "))
circumference=2*3.14*r
print("Circumference is",circumference)

# Write a program to find the perimeter of a triangle.
a=int(input("Enter side 1: "))
b=int(input("Enter side 2: "))
c=int(input("Enter side 3: "))
perimeter=a+b+c
print("Perimeter is",perimeter)

# Write a program to find the perimeter of a parallelogram.
a=int(input("Enter side a: "))
b=int(input("Enter side b: "))
perimeter=2*(a+b)
print("Perimeter is",perimeter)

# Write a program to find the perimeter of a rhombus.
a=int(input("Enter the side: "))
perimeter=4*a
print("Perimeter is",perimeter)

# Write a program to find the perimeter of a regular pentagon.
a=int(input("Enter the side: "))
perimeter=5*a
print("Perimeter is",perimeter)

# Write a program to find the perimeter of a regular hexagon.
a=int(input("Enter the side: "))
perimeter=6*a
print("Perimeter is",perimeter)

# Write a program to find the perimeter of a trapezium.
a=int(input("Enter side a: "))
b=int(input("Enter side b: "))
c=int(input("Enter side c: "))
d=int(input("Enter side d: "))
perimeter=a+b+c+d
print("Perimeter is",perimeter)

# Write a program to find the perimeter of an equilateral triangle.
a=int(input("Enter the side: "))
perimeter=3*a
print("Perimeter is",perimeter)


print("CUBE PROBLEMS")
# Write a program to find the volume of a cube.
a=int(input("Enter the side: "))
volume=a**3
print("Volume is",volume)

# Write a program to find the total surface area of a cube.
a=int(input("Enter the side: "))
tsa=6*a*a
print("Total Surface Area is",tsa)

# Write a program to find the lateral surface area of a cube.
a=int(input("Enter the side: "))
lsa=4*a*a
print("Lateral Surface Area is",lsa)

# Write a program to find the cube of a given number.
n=int(input("Enter a number: "))
cube=n**3
print("Cube is",cube)

# Write a program to check whether a number is a perfect cube.
n=int(input("Enter a number: "))
root=round(n**(1/3))
if root**3==n:
    print("Perfect Cube")
else:
    print("Not a Perfect Cube")

# Write a program to find the sum of cubes of two numbers.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum_cubes=a**3+b**3
print("Sum of cubes is",sum_cubes)

# Write a program to find the difference of cubes of two numbers.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
diff_cubes=a**3-b**3
print("Difference of cubes is",diff_cubes)

# Write a program to print cubes from 1 to N.
n=int(input("Enter N: "))
for i in range(1,n+1):
    print(i**3)

# Write a program to find the cube root of a number.
n=int(input("Enter a number: "))
cube_root=n**(1/3)
print("Cube Root is",cube_root)

# Write a program to find the largest cube less than or equal to N.
n=int(input("Enter N: "))
i=1
while (i+1)**3<=n:
    i+=1
print("Largest cube less than or equal to N is",i**3)