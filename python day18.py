# WHILE LOOPS



# Write a while loop that prints numbers 1 through 100.
i=1
while(i<=100):
    print(i)
    i+=1
    
    
# Given an integer, use a while loop to calculate the sum of its digits. 
num = 123
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print(sum_digits)  


# Reverse a number using a while loop (without converting to string).
num = 1234
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)   # 4321


# Determine if a number is a palindrome using a while loop.
def is_palindrome(num):
    original = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return original == reversed_num



# Count the number of digits in a given integer using a while loop.
num = 9876
count = 0
while num != 0:
    num //= 10
    count += 1
print(count)   # 4



# Generate the first N numbers of the Fibonacci sequence using a while loop.
n = 10
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
# Output: 0 1 1 2 3 5 8 13 21 34



# What is an infinite loop? Give an example and how to prevent it.
i = 1
while i > 0:   # always true
    print(i)
    i += 1
    

# Write a while loop that keeps asking the user for a positive integer until they enter one.
while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num > 0:
            break
        else:
            print("Not positive. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
        
        
# Implement GCD using a while loop OR Implement the Euclidean algorithm for finding GCD using a while loop.

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a



# Allow a user 3 attempts to enter a PIN. After 3 wrong attempts, lock the account.
correct_pin = "1234"
attempts = 0
while attempts < 3:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access granted")
        break
    else:
        attempts += 1
        print(f"Wrong PIN. {3-attempts} attempts left.")
else:
    print("Account locked.")
    
    
    
    
    
# Given a sorted list, remove duplicates in‑place and return the new length – using only a while loop. OR Remove duplicates from sorted list (in‑place)
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    j = 1
    while j < len(nums):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1



# Explain the difference between break and continue in a while loop. Provide examples.

# The 'break' statement exits the loop entirely, while the 'continue' statement skips the current iteration and moves to the next one.
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue   # skip print for 3
    if i == 4:
        break      # stops loop at 4
    print(i)       # prints: 1, 2
    
    
    
#Generate a random number (1‑100). Let the user guess with hints "too high" / "too low". Use a while loop.
import random
secret = random.randint(1, 100)
guess = None
while guess != secret:
    guess = int(input("Guess: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
print("Correct!")



# Print a 5×5 multiplication table using nested while loops.
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(f"{i*j:3}", end=" ")
        j += 1
    print()
    i += 1
    
    
    
# What is the time complexity of the following while loop?
i = 1
while i < n:
    i *= 2
    