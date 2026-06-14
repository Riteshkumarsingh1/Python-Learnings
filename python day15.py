# create a python program that greets the user by good morning sir  using time module

import time
current_time = time.localtime()
hour = current_time.tm_hour
if (hour<12):
    print("Good Morning Sir")
else:
    if(hour<18):
        print("Good Afternoon Sir")
    else:
        print("Good Evening Sir")