
#1
count = 0

def bump():
    global count
    count += 1

def value():
    return count


#2
def make_counter():
    counter = 0

    def add_to_counter():
        nonlocal counter
        counter += 1
        print(counter)
    return add_to_counter

#3
#local
#enclosing
#global

#4
#we defined list as a variable and now its not callable
# 
# the correct way would be to name it differently 

#5
#see files mathutils and main

#6
#see file tools

#7
from datetime import datetime as dt
print(dt.now())

#8
def public_names(m):
    items = dir(m)
    return [i for i in items if i[0] != "_"]


#9

# setting a parameter as a list by default is risky since
# it stores the values every time it runs
# the fix would be to create a global list and get that as a parameter

#10
#added, see folder

