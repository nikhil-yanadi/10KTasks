1. List
========
A list is an ordered and mutable (changeable) collection in Python. It can store elements of different data types and allows duplicate values.
Features
         Ordered
         Mutable
         Allows duplicates
         Indexed
         Can contain mixed data types
Syntax
      fruits = ["apple", "banana", "mango"]
      Example
      numbers = [10, 20, 30]
      numbers.append(40)
      numbers[0] = 100
      print(numbers)
      # Output: [100, 20, 30, 40]

2. Nested List:
==============
A nested list is a list that contains one or more lists as its elements. It is commonly used to represent tables, matrices, and multidimensional data.
        
Features
        List inside another list
        Access elements using multiple indexes
        Useful for 2D and 3D data
Syntax
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Example
matrix = 
[[10, 20],
    [30, 40]]

print(matrix[0][1])   # 20
print(matrix[1][0])   # 30
Traversing a Nested List
matrix = [
    [1, 2],
    [3, 4]
]
for row in matrix:
    for value in row:
        print(value)
3. Tuple
========
A tuple is an ordered but immutable (unchangeable) collection.
Features
        Ordered
        Immutable
        Allows duplicates
        Faster than lists
        Indexed
Syntax
      colors = ("red", "green", "blue")
      Example
      numbers = (10, 20, 30)
      
      print(numbers[1])
      print(len(numbers))
      
      Output
            20
            3 
4. Set
======
A set is an unordered collection of unique elements.

Features
        Unordered
        Mutable
        No duplicate values
        No indexing
        Useful for mathematical operations
Syntax
        nums = {1, 2, 3}
        Example
        numbers = {10, 20, 30, 20}        
        print(numbers)
Output
      {10, 20, 30}
      Common Operations
      a = {1, 2, 3}
      b = {3, 4, 5}
      
      print(a | b)   # Union
      print(a & b)   # Intersection
      print(a - b)   # Difference
5. Dictionary
=============
A dictionary stores data as key-value pairs.
Features
        Mutable
        Ordered (Python 3.7+)
        Keys must be unique
        Fast lookup using keys
Syntax
      student = {"name": "Nikhil", "age": 22, "course": "Python"}
      Example
      student = {
          "name": "Nikhil",
          "age": 22
      }
      print(student["name"])
      student["age"] = 23
      student["city"] = "Hyderabad"
      print(student)

Output
      Nikhil
      {'name': 'Nikhil', 'age': 23, 'city': 'Hyderabad'}
