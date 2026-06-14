# match case statement
# The match statement (often called structural pattern matching) is like a powerful switch-case on steroids. It compares a value against multiple patterns and executes the first matching block.

# Key Features
# Feature                 	Example
# Literal matching	        case 42:
# OR pattern	                case "red" | "blue":
# Capture variable	        case x: (captures the value into variable x)
# Wildcard (default)	        case _:
# Sequence unpacking	        case [a, b]:
# Mapping unpacking	        case {"name": n, "age": a}:
# Guard (condition)	        case x if x > 0:
# Type matching	            case int(): or case str():



x = int(input("enter the value of x: "))
# x is the value to be matched against the patterns in the case statements.
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # if x is 1
    case 1:
        print("x is one")
    # if x is 2 or 3
    case 2 | 3: 
        print("x is two or three")
    case _:
        print("x is something else")

# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # if x is 1
#     case_ if x!=90:
#     print("x is not 90")                   ONLY FOR REPPLIT USERS NOT VS CODE USERS
#     # if x is 2 or 3
#     case_ if x!=80 : 
#     print("x is not 80")
#     case _:
#     print("x is something else")

# match x:
#     case 0:
#         print("x is zero")
#     case 90:
#         pass  # or handle 90
#     case 80:
#         pass
#     case _:
#         if x != 90:
#             print("x is not 90")
#         if x != 80:
#             print("x is not 80")
#         else:
#             print ("x is something else")
