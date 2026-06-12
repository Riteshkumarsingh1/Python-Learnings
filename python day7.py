print("hello world")
print("my name is rajan gupta")


print("ritesh kumar singh")

print(1137)

name = "ritesh"
age = 20
price = 20.22
print(name, age, price)
print(type(name))
print(type(age))
print(type(price))

age = 39
old = False
a = None
print(type(old))
print(type(a))

# SUM
a = 3
b = 9
sum = a+b
print(sum)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b) #power
print(a%b) #remainder


# relational operator

print(a==b) #False
print(a!=b)#True
print(a<b)#True
print(a>=b)#False

# Assignment Operators 
num = 10
num = num+10 #10+10 =20

num += 10
num -= 10
num *= 12
num /= 3
num %= 2
print("num:", num)


# Logical Operators
a = 12
b = 29
# print(not (a>b)) #True
# print( not (a<b)) #False

val1 = False
val2 = True
print("and operator:", val1 and val2)
# print("OR operator:", val1 or val2)


#Typecasting
a ="3"
b = 4.001
# sum = (a+b)
print (type(a))

# Input 

name = input("enter your name: ")
print("welcome", name)

name = input("enter your caste: ")
print("your caste is:", name)

val = input("enter some value:")
print(type(val),val)
val = int (input("my name is ritesh kumar singh:"))
print(type(val))


name = input ("enter your name:")
age = input ("enter your age:")
marks = input("enter your marks:")

print("welcome:", name)
print("age:", age)
print("your marks:", marks)


a = int (input("enter first number:"))
b = int(input("enter second number:"))
sum = a+b
print("sum=", sum)


a = int(input("enter one side of square:"))
area = a**2
print("Area of given square=",area)


a = float(input("enter the number:"))
b = float(input("enter the number:"))
avg = (a+b)/2
print("Avg of given numbers=", avg)

a= int(input("enter first no:"))
b= int(input("enter second no:"))
print(a>b)