# This is a simple calculator program that performs basic arithmetic operations on two numbers, a and b. The program calculates and prints the sum, difference, product, and quotient of a and b.
# a=5
# b=9

# print("the value of", a, "+", b, "is", a+b)
# print("the value of", a, "-", b, "is", a-b)
# print("the value of", a, "*", b, "is", a*b)
# print("the value of", a, "/", b, "is", a/b) 

num1= int(input("enter first number: "))
num2= int (input("enter second number: "))

add= num1+num2
print("the value of", num1, "+", num2, "is", add)
sub= num1-num2
print("the value of", num1, "-", num2, "is", sub)
mul= num1*num2
print("the value of", num1, "*", num2, "is", mul)
div= num1/num2
print("the value of", num1, "/", num2, "is", div)
exponent= num1**num2
print("the value of", num1, "**", num2, "is", exponent)