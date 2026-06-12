# String in python

name ="!!!rajan shyam!!!!"
print ("hey", name)
# String concatenation
first_name= "rajan"     
last_name= "shrestha"
full_name= first_name + " " + last_name
print("full name is", full_name)
# String formatting
age= 25 
print("my name is {} and i am {} years old".format(full_name, age))

# String indexing and slicing
message= "hello world"  
print(message[0])  # prints 'h'
print(message[6])  # prints 'w'
print(message[-1])  # prints 'd'  // negative indexing starts from the end of the string
print(message[0:5])  # prints 'hello'  // slicing from index 0 to 4 (5 is exclusive)
print(message[6:11])  # prints 'world'  // slicing from index 6 to 10 (11 is exclusive)

# loop through string
for char in message:
    print(char)
    
# string methods
print(message.upper())  # prints 'HELLO WORLD'
print(message.lower())  # prints 'hello world'
print(message.capitalize())  # prints 'Hello world'
print(message.title())  # prints 'Hello World'  
print(name.upper())  # prints 'RAJAN'
print(name.rstrip("!"))  # prints 'rajan shyam'  // removes any leading or trailing whitespace
print(name.lstrip("!"))  # prints 'rajan shyam'  // removes any leading whitespace
print(name.replace("!", ""))  # prints 'rajan shyam'  // replaces all occurrences of "!" with an empty string
print (name.count("!"))  # prints 8  // counts the number of occurrences of "!" in the string
print(name.find("a"))  # prints 2  // returns the index of the first occurrence of "a" in the string, or -1 if not found
print(name.find("z"))  # prints -1  // returns -1 since "z" is not found in the string
print(name.split("!"))  # prints ['rajan', 'shyam']  // splits the string into a list of substrings based on the delimiter "!"
print(name.strip("!"))  # prints 'rajan shyam'  // removes any leading or trailing "!" characters from the string
print(name.endswith("!"))  # prints True  // returns True if the string ends with "!", otherwise returns False
print(name.startswith("!"))  # prints True  // returns True if the string
print(name.isalpha())  # prints False  // returns False since the string contains spaces and "!" characters
print(name.isalnum())  # prints False  // returns False since the string contains spaces and "!" characters
print(name.isdigit())  # prints False  // returns False since the string does not contain only digits
print(name.isprintable())  # prints True  // returns True since all characters in the string are printable
print(name.isspace())  # prints False  // returns False since the string contains non-whitespace characters 
print(name.istitle())  # prints False  // returns False since the string is not in title case (first letter of each word is not capitalized )
print(name.swapcase())  # prints 'RAJAN SHYAM'  // returns a new string with uppercase letters converted to lowercase and vice versa            
print(name.zfill(20))  # prints '0000000000rajan shyam'  // returns a new string padded with zeros on the left to fill a total width of 20 characters
print(name.center(20, "*"))  # prints '****rajan shyam****'  // returns a new string centered within a total width of 20 characters, padded with "*" on both sides
print(name.ljust(20, "*"))  # prints 'rajan shyam**********'  // returns a new string left-justified within a total width of 20 characters, padded with "*" on the right
print(name.rjust(20, "*"))  # prints '**********rajan shyam'  // returns a new string right-justified within a total width of 20 characters, padded with "*" on the left
print(name.partition(" "))  # prints ('rajan', ' ', 'shyam')  // splits the string into a tuple of three parts: the part before the first occurrence of the separator " ", the separator itself, and the part after the separator           
print(name.rpartition(" "))  # prints ('rajan', ' ', 'shyam')  // splits the string into a tuple of three parts: the part before the last occurrence of the separator " ", the separator itself, and the part after the separator