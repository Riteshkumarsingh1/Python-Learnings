# LIST IN PYTHON

# lists are ORDERED, MUTABLE AND DYNAMIC ARRAY
list =[1,2,3,4,5,6,7,8, 'rajan', True]
print(list)
empty = []                     
numbers = [1, 2, 3]            
mixed = [1, "hello", 3.14]     
nested = [[1, 2], [3, 4]]      
constructor = list("abc")      # ['a', 'b', 'c']
range_list = list(range(5))    # [0,1,2,3,4]


# ACCESSING VIA INDEXING
lst = [10, 20, 30, 40]
print(lst[0])    # 10   (positive index)
print(lst[-1])   # 40   (negative index from end)


# SLICING [start:stop:step]
# Returns a new list (shallow copy).
lst = [0,1,2,3,4,5]
lst[1:4]    # [1,2,3]
lst[:3]     # [0,1,2]
lst[::2]    # [0,2,4]
lst[::-1]   # [5,4,3,2,1,0]  (reverse)


# LENGTH OF STRING
len(list) 

# METHODS IN LIST
# 1. APPEND VS EXTEND
a = [1,2]
a.append([3,4])   # [1,2,[3,4]]
a = [1,2]
a.extend([3,4])   # [1,2,3,4]

# 2.LIST COMPREHENSION
# Interview tip: List comprehensions are faster than manual loops because they are optimized in C.

# [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]           # [0,1,4,9,...]
evens = [x for x in range(20) if x % 2 == 0]
matrix = [[j for j in range(3)] for i in range(4)]   # nested

# With if-else:
labels = [ "even" if n%2==0 else "odd" for n in range(5) ]


# COPYING LIST - SHALLOW VS DEEP
# Assignment (=) – does not copy; both names refer to same list.
# Shallow copy – new list, but elements are references to same objects.
# new = lst.copy()
# new = lst[:]
# new = list(lst)
# Deep copy – recursively copies nested objects.
import copy
original = [[1,2], [3,4]]
shallow = original.copy()
shallow[0][0] = 99
print(original[0][0])   # 99 → affected!

deep = copy.deepcopy(original)
deep[0][0] = 999
print(original[0][0])   # still 99, unaffected



# CONCATINATION AND REPETEATION

[1,2] + [3,4]     # [1,2,3,4]
[1,2] * 3         # [1,2,1,2,1,2]


#  in  OPERATOR (MEMBERSHIP TEST)

if 'ram' in ['mahesh','mukesh', 'rajan', 'rakesh', 'ram']:
    print("found")
    
    
# UNPACKING 

a, b, *rest = [1,2,3,4,5]
# a=1, b=2, rest=[3,4,5]

*head, tail = [1,2,3]   # head=[1,2], tail=3  

# USING * FOR FUNCTION ARGUMENTS
def func(a,b,c):
    print(a,b,c)
args = [1,2,3]
func(*args)   # unpacks list as positional arguments

# SORTING WITH key 
items = ["apple","banana","cherry"]
items.sort(key=len)               # by length

students = [("John", 20), ("Jane", 18)]
students.sort(key=lambda x: x[1]) # sort by age

# sorted() RETURNS NEW LIST , ORIGINALLY UNCHANGED
new = sorted(original, key=len, reverse=True)


# LIST ASS STACK 
stack = []
stack.append(1); stack.append(2)
stack.pop()    # returns 2


# LIST AS QUEUE
from collections import deque
q = deque([1,2,3])
q.append(4)
q.popleft()    # O(1)



# PITFALLS:-

# MODIFYING LIST WHILE ITERATING  NOT DONE EITHER CREATE NEW COPY OF LIST
lst = [1,2,3,4]
for i in lst:
    if i%2==0:
        lst.remove(i)   # Skipping elements – BAD
# Better: iterate over copy or use list comprehension
lst = [i for i in lst if i%2 != 0]

# USING MUTABLE DEFAULT ARGUMENTS (list as  default)
def add_to(item, lst=[]):   # BUG: list persists across calls
    lst.append(item)
    return lst
# Fix:
def add_to(item, lst=None):
    if lst is None: lst = []
    lst.append(item)
    return lst

# USING join() INSTEAD OF += IN LOOPS FOR STRING
# Slow: O(n^2)
s = ""
for word in ["a","b","c"]:
    s += word
# Fast:
"".join(["a","b","c"])





# Function	                 Description

# len(lst)	                 Length  
# max(lst), min(lst)	     Extreme values
# sum(lst)	                 Sum (numbers)
# any(lst), all(lst)	     Boolean conditions
# sorted(lst)	             Returns new sorted list
# reversed(lst)	             Returns iterator (use list(reversed(lst)))
# enumerate(lst)	         Index‑value pairs
# zip(lst1, lst2)	         Pairwise tuples
# filter(func, lst)	         Lazy filter
# map(func, lst)	         Lazy transformation