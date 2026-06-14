# # conditional statements 

# a = int(input("enter your age: "))
# print("your age is", a)

# # conditional operators
# # == equal to
# #( != not equal to  ) 
# # > greater than
# # < less than
# # >= greater than or equal to
# # <= less than or equal to

# print(a == 18)  # prints True if a is equal to 18, otherwise prints False
# print(a != 18)  # prints True if a is not equal to 18, otherwise prints False
# print(a > 18)  # prints True if a is greater than 18, otherwise prints False
# print(a < 18)  # prints True if a is less than 18, otherwise prints False
# print(a >= 18)  # prints True if a is greater than or equal to 18, otherwise prints False
# print(a <= 18)  # prints True if a is less than or equal to 18, otherwise prints False  

# print(a > 18 and a < 60)  # prints True if a is greater than 18 and less than 60, otherwise prints False
# print(a < 18 or a > 60)  # prints True if a is less than 18 or greater than 60, otherwise prints False
# print(not(a > 18 and a < 60))  # prints True if a is not greater than 18 and less than 60, otherwise prints False   

# print("you are eligible to vote" if a >= 18 else "you are not eligible to vote")  # prints "you are eligible to vote" if a is greater than or equal to 18, otherwise prints "you are not eligible to vote"  
# print("you are a child" if a < 18 else "you are an adult")  # prints "you are a child" if a is less than 18, otherwise prints "you are an adult"


# NESTED IF-ELSE STATEMENTS
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print(num, "number is zero")
    else:
        if num == 999:
            print(num, "is a special number")
        else:
            if num <= 9:
                print(num, "is a single digit number")
            else:
                if num <= 99:
                    print(num, "is a two digit number")
                else:
                    print(num, "is a three or more digit number")
else:
    print(num, "is a negative number")
