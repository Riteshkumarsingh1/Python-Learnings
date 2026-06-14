# typecasting

a= 10
b= 20.5    
c= "Hello"
print(type(a))
print(type(b))  
print(type(c))
print(int(a)+int(b))  # explicit typecasting b to int before addition
print(float(a)+float(b))  # explicit typecasting a to float before addition
print(a+b)  # no typecasting, will perform addition as is and implicitly convert a to float before addition
print(str(a)+str(b))  # explicit typecasting both a and b to string before concatenation
