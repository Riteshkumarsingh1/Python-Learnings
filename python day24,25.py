# TUPLES IN PYTHON

# Memory: Tuples have less overhead than lists (no extra capacity for growth). Use sys.getsizeof().
# Speed: Creating tuples and iterating over them is slightly faster because Python knows size is fixed.
# Creation: tuple([1,2,3]) vs (1,2,3) – literal is faster.


tup=(1,2,3,1)
print(type(tup), tup)

# NOTE agar yha  tup=(1) bs hota tb run krne pr  type integer batata so  comma after single entry is must here like  tup=(1,) for its tuple type in output


#  TUPLE CREATION
empty = ()
single = (5,)                 # Note: comma required! (5) is int
multiple = (1, 2, 3)
mixed = (1, "hello", 3.14)
nested = ((1,2), (3,4))
from_list = tuple([1,2,3])    # (1,2,3)
from_string = tuple("abc")    # ('a','b','c')
without_parentheses = 1, 2, 3 # Packing – also a tuple


# ACCESSING ELEMENTS (indexing and  slicing)
# Same as lists – [index], [-1], slicing [start:stop:step].
t = (10, 20, 30, 40, 50)
t[1]      # 20
t[-1]     # 50
t[1:4]    # (20,30,40)
t[::-1]   # (50,40,30,20,10)

# LENGTH
len(t)   # 5

# CONCATENATION AND REPETITION
(1,2) + (3,4)     # (1,2,3,4)  – new tuple
(1,2) * 3         # (1,2,1,2,1,2)

# IMMUTABLITY ;;;;;
#  Cannot modify once created
t = (1,2,3)
t[0] = 99          # TypeError: 'tuple' object does not support item assignment
t.append(4)        # AttributeError: 'tuple' object has no attribute 'append'

# But if a tuple contains mutable objects (e.g., list), those objects can be mutated:
t = (1, [2,3], 4)
t[1].append(99)    # OK – modifies the list inside tuple
print(t)           # (1, [2,3,99], 4)
# But still cannot reassign t[1] = [5]





# METHODS IN TUPLE:::::::::

# Method     	           Description	                                                   Example
# count(x)	               Return number of occurrences of x	                           (1,2,2,3).count(2) → 2
# index(x, start, end)	   Return first index of x (raises ValueError if not found)	       (1,2,3).index(2) → 1

# Note: No append, remove, pop, sort, etc.



# PACKING AND UNPACKING   :: tuples are automatically created

# packing
a = 1, 2, 3         # a is (1,2,3)

# unpacking
t = (10, 20, 30)
x, y, z = t         # x=10, y=20, z=30

# Extended unpacking with *
a, b, *rest = (1,2,3,4,5)   # a=1, b=2, rest=[3,4,5]
*head, tail = (1,2,3)       # head=[1,2], tail=3


# SWAPING VARIABLE : (tuple unpacking trick)
a, b = 5, 10
a, b = b, a         # swap – elegant!




# TUPLES AS DICTIONARY KEYS
# Because tuples are immutable (and hashable if all elements are immutable), they can be keys in dictionaries.

locations = {}
locations[(40.7128, -74.0060)] = "NYC"
locations[(34.0522, -118.2437)] = "LA"
print(locations[(40.7128, -74.0060)])  # NYC


# TUPLE CONTAINING LIST IS NOT HASHABLE nethir in dictionary
{(1, [2,3]): "value"}   # TypeError: unhashable type: 'list'



# Tuple comprehension? No – but use generator expression
# This is a generator expression, not tuple comprehension
gen = (x**2 for x in range(5))
t = tuple(gen)        # (0,1,4,9,16)

# Converting between list and tuple
lst = [1,2,3]
t = tuple(lst)        # (1,2,3)
lst2 = list(t)        # [1,2,3]

# in operator – membership test
if 2 in (1,2,3):      # O(n)
    print("found")
    
# * operator for repetition – watch out with mutable contents
t = ([1,2],) * 3      # three references to same list!
t[0].append(99)
print(t)              # ([1,2,99], [1,2,99], [1,2,99])
# Fix: tuple([1,2] for _ in range(3))
#

# Returning multiple values from function (automatic tuple)
def divmod(a, b):
    return a // b, a % b   # returns tuple

result = divmod(10, 3)     # (3, 1)
quot, rem = divmod(10, 3)  # unpacking




# VIP SECTION




# 10. Common Interview Questions & Answers
# Q1: Why are tuples faster than lists?
# Tuples are immutable, so Python can allocate exact memory without over‑allocation.

# Immutability allows for optimizations like constant folding and reduced reference counting overhead.

# Iteration and indexing are slightly faster.

# Q2: Can a tuple be used as a dictionary key if it contains a list?
# No – because the tuple would not be hashable. All elements must be hashable (immutable). A list inside makes the tuple unhashable.

# Q3: How to sort a tuple? (Can’t sort in‑place)
# python
# t = (3,1,2)
# sorted_t = tuple(sorted(t))   # returns new tuple (1,2,3)
# Q4: What is the difference between (1) and (1,)?
# (1) is an integer with parentheses for grouping; (1,) is a tuple with one element.

# Q5: How to add an element to a tuple?
# You cannot modify. Create a new tuple by concatenation:

# python
# t = (1,2,3)
# t = t + (4,)      # (1,2,3,4)
# Q6: What is tuple unpacking? Give example.
# Assigning tuple elements to individual variables. Also used in for loops:

# python
# pairs = [(1,2), (3,4)]
# for a,b in pairs:
#     print(a,b)
# Q7: What is a namedtuple? Why use it?
# A factory function that creates tuple subclasses with named fields. Provides readability without custom class overhead. Useful for simple data containers.

# Q8: Memory comparison: list of tuples vs dict of tuples? (not exactly)
# Usually answer: use tuple as key when needed; if just storing records, list of namedtuples is often fine.

# Q9: Can you have a tuple of tuples? Yes.
# python
# t = ((1,2), (3,4))
# Q10: What happens if you try to assign to an element of a tuple that contains a list?
# Assignment to the tuple element fails (TypeError), but you can modify the list inside because it’s mutable.

# 11. Summary for Interview Cram
# Core: Immutable, ordered, hashable (if elements are). Use for fixed data, dictionary keys, multiple returns.

# Methods: Only count() and index().

# Creation: Parentheses optional but comma mandatory for single‑element.

# Unpacking is powerful – swap variables, iterate over pairs.

# Performance: Less memory, slightly faster than lists.

# Named tuples add readability without mutability.

# Pitfalls: Single‑element comma, mutable elements inside, repetition with mutable objects.

# Practice tasks for interview:

# Write a function that returns min and max of a list as a tuple.

# Convert list of key‑value pairs to dict using tuple unpacking.

# Use tuple as dict key to store coordinates.

# Explain why {} can’t be used as a key but () can.

# Tuples are elegant and show understanding of immutability – a sign of clean Python code.

