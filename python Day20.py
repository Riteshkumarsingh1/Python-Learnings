# Function in python

# def animal(name, sound):
#     return f"the {name} sounds like {sound}"
# print (animal("lion", "roars"))

# # o/p = the lion sounds like roars



# def college (teacher, student,staff):
#     return f"the {teacher} teaches the {student} and staff maintains the {staff}"
# print(college  ("Mr. Smith", "students", "library"))



#  average nikalne ka function
# def average(numbers):
#     return sum (numbers)/len(numbers)
# print (average([12, 13, 14, 15, 16, 17, 18]))
# print (average([12, 13, 14, 15, 16, 17, 18, 19]))            
# #  note h m yha  numbers ka list pass kar rhe h or sum and len ka use krke average nikal rhe h, list isliye pass kr rhe h kyuki sum and len ka use krne k liye iterable chahiye or list iterable h



# average by taking user input
def average_user_input():
    numbers = []
    while True:
        try:
            num = float(input("Enter a number (or type 'done' to finish): "))
            numbers.append(num)
        except ValueError:
            break
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0