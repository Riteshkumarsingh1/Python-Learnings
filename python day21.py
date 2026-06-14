# FUNCTION ARGUMENTS




# Positional arguments
def add(a, b):
    return a + b
print (add(5, 3))  # Output: 8


# default arguments
def greet(name="Guest"):
    return f"Hello, {name}!"
print (greet())  # Output: Hello, Guest!
print (greet("Alice"))  # Output: Hello, Alice!


# keyword arguments
def describe_pet(pet_name, animal_type="dog"):
    return f"I have a {animal_type} named {pet_name}."
print (describe_pet("Buddy"))  # Output: I have a dog named Buddy.
print (describe_pet("Whiskers", "cat"))  # Output: I have a cat named Whiskers.



# variable length arguments

# *args – captures extra positional arguments as a tuple
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))      # 6
print(sum_all())             # 0

# **kwargs – captures extra keyword arguments as a dictionary
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)   # name: Alice \n age: 30



# Required Arguments 
# Required arguments are parameters in a function that do not have a default value. The caller must provide a value for them; otherwise, Python raises a TypeError.

def greet(first_name, last_name):   # both are required
    print(f"Hello, {first_name} {last_name}")

greet("John", "Doe")    # OK
greet("John")           # TypeError: missing 1 required positional argument: 'last_name'



def average (a,b):
    return (a+b)/2
print(average(8,9))