# for loops in python
# The for loop in Python is used to iterate over a sequence (like a list, tuple, string, dictionary, or range) and execute a block of code for each item.



# USING RANGE NUMERIC LOOPS
# for i in range(20): 0 se 19 tk print kar k dega ye (n-1) tk jayega bs ye
#     print(i)
# for i in range(1,120):    1 se 119 tk print kar k dega ye
#         print(i)


# ITERATE OVER STRING
# name = "Ritesh Kumar Singh"
# for i in name:
#  print(i)


# ITERATE OVER LISTS
# animals = ["cat", "dog", "rabbit"]
# for animal in animals:
#     print(animal)
#     for i in animal:
#         print(i)



# ITERATE OVER DICTIONARY
# student = {"name": "Ritesh", "age": 20, "city": "New York"}
# for key in student:       
#     print(key, student[key])


# ITERATE OVER TUPLE
# numbers = (1, 2, 3, 4, 5)
# for n in numbers:
#     print(n)



# # NESTED FOR LOOPS
# for i in range(3):
#     for j in range(2):
#         print(i, j)   


# USING enumerate() to get index and value
# fruits = ["apple", "banana", "cherry"]    
# for index, fruit in enumerate(fruits):
#     print(index, fruit)


# USING zip() to iterate over multiple sequences
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# for name, age in zip(names, ages):
#     print(name, age)


# using step in range()
# for i in range(0, 10, 2):  # prints even numbers from 0 to 8
#     print(i)

# for i in range(0, 10, 3):  # prints numbers from 0 to 10 with a step of 3 or divisible by 3
#     print(i)