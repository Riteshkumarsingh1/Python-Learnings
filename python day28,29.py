# "String formatting = variables ko string mein safe aur readable tarike se place karna."

name = "Aarav"
score = 95

# Simple
print(f"Hello {name}, score {score}")

# Expression
print(f"Next year: {score + 5}")

# Format specifier (2 decimal places)
pi = 3.14159
print(f"Pi = {pi:.2f}")

# Call method
print(f"Uppercase: {name.upper()}")

# Alignment
print(f"{'Left':<10} | {'Right':>10}")







# Docstring = documentation string – ek string hoti hai jo function, class, ya module ke turant baad likhi jaati hai, uss cheez ka description dene ke liye.

# Kaise likhte hain: Triple quotes """ ya ''' ke andar.



def add(a, b):
    """Is function mein do numbers add hote hain."""
    return a + b

print(add.__doc__)   # Output: Is function mein do numbers add hote hain.








# PEP 8 Kya Hai?

# PEP 8 = Python Enhancement Proposal #8 – Python code likhne ka style guide (formatting rules). Batata hai ki code kaise dikhna chahiye – indentation, spacing, naming, etc

# Kyun zaroori hai?

# Code readable aur consistent hota hai
# Team mein sab same style follow karte hain
# Code review easy ho jaata hai
# Python community ka standard

# Key Rules (Interview Must-Know)



# 1. Indentation – 4 spaces per level (NO tabs)
# ✅ Correct
def func():
    if True:
        print("4 spaces")

# ❌ Wrong – tab use kiya
def func():
	if True:
		print("tab")




# 2. Line length – Maximum 79 characters
# ✅ Short line
result = calculate_sum(a, b, c)

# ❌ Too long (split karo)
result = calculate_sum(very_long_variable_name_1, very_long_variable_name_2, very_long_variable_name_3)




# 3. Blank lines
# Top-level functions/classes ke beech 2 blank lines
# Class ke andar methods ke beech 1 blank line
import math

# 2 blank lines above
def func1():
    pass

# 2 blank lines above
def func2():
    pass

class MyClass:
    # 1 blank line above method
    def method1(self):
        pass
    
    # 1 blank line above method
    def method2(self):
        pass



# 4. Imports – Separate lines, placed at top

# ✅ Correct
import os
import sys
from math import sqrt

# ❌ Wrong – multiple imports on same line
import os, sys
# Order:

# Standard library imports

# Third-party imports

# Local application imports

# (Each group separated by blank line)



# 5. Whitespace in expressions
# python
# ✅ Correct
spam(ham[1], {eggs: 2})
i = i + 1
x = x*2 - 1

# ❌ Wrong
spam( ham[ 1 ], { eggs: 2 } )
i=i+1


# 6. Naming conventions
# Type	Convention	Example
# Variable	lowercase_with_underscores	my_var
# Function	lowercase_with_underscores	calculate_sum()
# Class	CapWords (CamelCase)	MyClass
# Constant	UPPERCASE_WITH_UNDERSCORES	MAX_VALUE
# Private attribute	_leading underscore	_internal
# "Private" (name mangling)	__double leading	__private


# 7. Comparisons
# python
# ✅ Correct – compare with None using 'is'
if x is None:
    pass

# ❌ Wrong
if x == None:
    pass

# ✅ Correct – boolean check
if is_valid:      # not if is_valid == True
    pass


# 8. Try/Except/Finally
# ✅ Specific exception
try:
    value = int(x)
except ValueError as e:
    print(f"Invalid: {e}")

# ❌ Bare except (catches everything, including KeyboardInterrupt)
try:
    value = int(x)
except:
    pass











#  How to check if code follows PEP 8?
#  Use pylint, flake8, or black (auto-formatter)



# Difference between _var, __var, var_?

# _var – internal use (weak "private")

# __var – name mangling (strong private)

# var_ – avoid keyword conflict (e.g., class_)

