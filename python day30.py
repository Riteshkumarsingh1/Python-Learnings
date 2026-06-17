# RECURSION


# function k andar function called recursion

# factorial of n
#  n! = n*(n-1)*(n-2).......1

def fact(n):     #created a function of factorial                   
    if n==1:          # given base condition
        return 1      # output for base condition
    else:             # main condition
        return n* fact(n-1)   # output for main condition and recursive call in it for factorial
    
    
print(fact(5)) #function being called by giving minimum input


# fibonacci no
# Fibonacci mein har number apne se pehle do numbers ka sum hota hai:
# 0, 1, 1, 2, 3, 5, 8...
def fib(n):
    # base case 2 stop condition
    if(n==0):
        return 0
    else:
        if n==1:
            return 1
        # recursive case 2 baar call ho  rha hai
        else: 
            return fib(n-1) + fib(n-2)
        
print (fib(6))        #output 8
    