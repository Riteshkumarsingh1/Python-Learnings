# SETS  and its METHODS IN PYTHON


#  SETS CREATION::::::::::::

# 1. Curly braces {} se (Khaali set nahi bana sakte isse, ye dict banega)
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'banana', 'cherry', 'apple'} (Order random hota hai)

# 2. set() constructor se (List/Tuple ko set mein convert karna)
numbers = set([1, 2, 3, 3, 4])  
print(numbers)  # Output: {1, 2, 3, 4} (Dekho 3 sirf ek baar aaya!)

# 3. Empty set (Sirf set() se banta hai, {} se nahi)
empty_set = set()
empty_dict = {}  # Ye set nahi, dictionary hai!
my_set = {1, 2, 3}




# METHODS IN SETS::::::::::::::::

# Add - Ek item daalna
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# Update - Multiple items daalna (list/tuple/dusra set)
my_set.update([5, 6, 7])
print(my_set)  # {1, 2, 3, 4, 5, 6, 7}

# Remove - Item hatao (Agar item nahi mila toh ERROR degi)
my_set.remove(4)  
# my_set.remove(10)  # ❌ KeyError

# Discard - Item hatao (Agar item nahi mila toh ERROR nahi degi, ignore karegi)
my_set.discard(10)  # ✅ Kuch nahi hoga, error nahi aayegi

# Pop - Random item hatao aur return karo (kyunki ordered nahi hai)
popped_item = my_set.pop()
print(popped_item)  # Kuch bhi aa sakta hai (e.g., 1)






# OPERATIONS IN SETS:::::::::::::


jan_customers = {"Rahul", "Priya", "Amit"}
feb_customers = {"Priya", "Sneha", "Vikram"}

common = jan_customers & feb_customers
print(common)  # Output: {'Priya'} (Sirf Priya dono mein hai)

only_jan = jan_customers - feb_customers
print(only_jan)  # Output: {'Rahul', 'Amit'} (Sirf January mein aaye)
names = ["Rahul", "Priya", "Rahul", "Amit", "Priya", "Rahul"]
unique_names = list(set(names))

print(unique_names)  # Output: ['Amit', 'Priya', 'Rahul'] (Order garanteed nahi hai)
immutable_set = frozenset([1, 2, 3])
# immutable_set.add(4)  # ❌ AttributeError (Add nahi kar sakte)

valid_ids = {101, 102, 103, 104}
if 101 in valid_ids:
    print("ID 101 valid hai!")  # Yeh turant print ho jayega, bahut fast
    
    # my_set.add([1,2,3])  # ❌ TypeError: unhashable type: 'list'
my_set.add((1,2,3))    # ✅ Allowed

old = {"Aarav", "Priya", "Rohit"}
new = {"Priya", "Sneha", "Vikram"}

continued = old & new          # {'Priya'}
left = old - new               # {'Aarav', 'Rohit'}
fresh_admission = new - old    # {'Sneha', 'Vikram'}













# examples

s1 ={1,2,5,4,3}
s2 ={6,7,9,8,3,4}

print(s1.union(s2))
s1.update(s2)                   # union operation
print(s1)

print(s1.intersection(s2))
s1.intersection_update(s2)       #intersection operation
print(s1)

print(s1.difference(s2))
print(s1 - s2)                     #difference operation
s1.difference_update(s2)       
print(s1)

print(s1.symmetric_difference(s2))
print (s1^s2)
s1.symmetric_difference_update(s2)   #symmetric_difference operation
print(s1)

print(s1.issuperset(s2))  # op: false  as s1 is not superset of s2

print (s1.issubset(s2))  # op: false as s1 here is not subset of s2

