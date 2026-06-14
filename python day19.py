# # BREAK AND CONTINUE STATEMENTS IN PYTHON


# # BREAK STATEMENT
# # The break statement is used to exit a loop prematurely when a certain condition is met.   
# for i in range(1, 10):
#     if i == 5:
#         break  # Exit the loop when i is 5
#     print(i)  # This will print numbers from 1 to 4


# while True:
#     number = int(input("Enter a number (0 to exit): "))
#     if number == 0:
#         break  # Exit the loop when the user enters 0
#     print(f"You entered: {number}")

# # CONTINUE STATEMENT
# # The continue statement is used to skip the rest of the loop body and move to the next iteration.
# for i in range(1, 10):
#     if i == 5:
#         continue  # Skip the rest of the loop body when i is 5
#     print(i)  # This will print numbers from 1 to 4, but not 5

# while True:
#     number = int(input("Enter a number (0 to exit): "))
#     if number == 0:
#         break  # Exit the loop when the user enters 0
#     if number % 2 == 0:
#         continue  # Skip the rest of the loop body for even numbers
#     print(f"You entered an odd number: {number}")    # This will only print odd numbers entered by the user
    
    
# # f"..." – Formatted string literal (f‑string)
# # The f prefix (or F) before the opening quote tells Python it’s an f‑string.
# # F‑strings allow embedded expressions inside curly braces {}.
# # Available from Python 3.6+.
# name = "Alice"
# age = 30
# print(f"Hello, {name}! You are {age} years old.")



# 0

# # DO WHILE LOOP STIMULATE HERE
# # Python does not have a built-in do-while loop, but we can simulate it using a while loop.
# # The code inside the loop will execute at least once, and then it will check the condition to determine if it should continue.

do = True
while do:
    number = int(input("Enter a number (0 to exit): "))
    if number == 0:
        do = False  # Set do to False to exit the loop
    else:
        print(f"You entered: {number}")
        