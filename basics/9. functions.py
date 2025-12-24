# function = A block of reusable code
# place () after the function name to invoke it 

def happy_bday(n,name): # Positonal arguments
    for i in range(n):
        print(f"Happy birthday to {name}") 

happy_bday(2,"yash")
# Output = Happy birthday to yash
#          Happy birthday to yash

# return = statement used to end a function
#           and send a result backt ot the caller

def add(x,y):
    z = x+y
    return z

def sub(x,y):
    z = x-y
    return z

def multi(x,y):
    z = x*y
    return z

def div(x,y):
    z = x/y
    return z

print(add(1, 2))
print(sub(1, 2))
print(multi(1, 2))
print(div(1, 2))

# a function to create a full name
def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("yash","khandelwal")
print(full_name)
# Output = Yash Khandelwal

# default arguments = A default value for certain parameter
#                     default is used when that argument is omitted
#                     make your functions more fexible, reduces # of arguments
#                     1. positional, 2.DEFAULT, 3. keyword, 4. arbitrary

def net_price(list_price,discount= 0,tax=0.05): # By doing this we can set deafult values to def func
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500,0,0.05))
# Output = 525.0

print(net_price(500, 0.1)) # we dont need to put default set values now
# Output = 472.5 

# import time
# def count(start, end):
#     for x in range(end ,start = 0):
#         print(x)
#         time.sleep(1)
#     print("DONE!")
# a = int(input("Enter starting time: "))
# b = int(input("Enter end time:"))
# count(b,a)

# keyword arguments = an argument preceded by an identifier
#                     helps with readablity
#                     order of arguments doesn't matter
#                     1. positional 2. defalut 3. KEYWORD 4. arbitrary
 
def hello (greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title = "Mr. ",last="Squarepants",first="Songebob") # By keyword arguments we can set any order 
# Output = Hello Mr. Songebob Squarepants
# hello(title = "Mr. ",last="Squarepants",first="Songebob","Hello")  # Positional arguments must come before keyword arguments
# Output = SyntaxError: positional argument follows keyword argument

# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator 
#            1. positional 2. default 3. keyword 4. ARBITRARY

# Starting with *args
def meow(*args): # it creates a tuple and starts adding into it can give multiple arguments
    print(type(args))
meow(1)
# Output = <class 'tuple'>

def add(*args): # now we can add multiple arguments into it 
    total = 0
    for arg in args: # this need not ot be args or arg its just what every one use we can like also use num with nums
        total += arg
    return total

print(add(1,2,3,4)) 
# Output = 10

# Another example on diplaying names

print("Your name is " ,end = "")
def display_name(*args):
    for arg in args:
        print(arg, end = " ")

display_name("yash","meowcat")
# Output = Your name is yash meowcat

print()

# Now onto **kwargs

def type_kwargs(**kwargs): 
    print(type(kwargs))  

type_kwargs()
# Output = <class 'dict'>

def print_address(**kwargs):
    for key , value in kwargs.items():
        print(f"{key:10}:{value}")

print_address(
    street="123 Fate St.",
    city="Detroit",
    state="MI",
    zip="54321"
)
# Output = street    :123 Fate St.
#                     city      :Detroit
#                     state     :MI
#                     zip       :54321

 
# def shipping_label(**kwargs, *args):   # args will come b4 kwargs cuz kwargs is keyword ones
#     pass
# Output = SyntaxError: arguments cannot follow var-keyword argument

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    for key , value in kwargs.items():
        print(f"{key:10}:{value}")

shipping_label("Dr.","Spongebob","Squarepasnts","III",
               street="123 Fate St.",
                city="Detroit",
                state="MI",
                 zip="54321")
# Output = Dr. Spongebob Squarepasnts III
#          street    :123 Fate St.
#          city      :Detroit
#          state     :MI
#          zip       :54321
