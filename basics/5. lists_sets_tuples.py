0# collection = single variable used to store multiple values
#     List = [] ordered and changeable. Duplicates OK
#     Set = {} unordered and immutable,  but Add/Remove OK. NO duplicates
#     Tuple = () ordred and changeable. Duplicate OK. FASTER

fruits = ["Apple","Orange","Banana","Coconut"]
print(type(fruits))

print(fruits[::-1])     # we can print then by index like (start:end:step)        # we can also use -1 to get reversed order
# output = ['Coconut', 'Banana', 'Orange', 'Apple']

# for loop in lists

for fruit in fruits:    # instead of i we used fruit here for better reading of code (ideal)
    print(fruit)      

# output =    Apple
#             Orange
#             Banana
#             Coconut


# print(dir(fruits))    # This function is used to get to know what we can do do with the collection specified
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# print(help(fruits))    # This to get help on specified collection(can be very usefull)

print(len(fruits))  # classic : used to get the len of the list 
# output = 4

print("apple" in fruits) # used to find if the given value is in the list will return a boolean

# as lists are changeable we can add new stuff in it by :-
fruits[0] = "pineapple"  # will add pineapple to index 0
print(fruits) 
# Output = ['pineapple', 'Orange', 'Banana', 'Coconut']
fruits.append("Watermelon")   # This will append Watermelon to end of the list
print(fruits)
# output = ['pineapple', 'Orange', 'Banana', 'Coconut', 'Watermelon']
fruits.remove("Orange") # This will remove Apple from the List
print(fruits)
# fruits.pop(2)  # will pop the object from index specified 
# print(fruits)
# Output = ['pineapple', 'Banana', 'Watermelon']
# output = ['pineapple', 'Banana', 'Coconut', 'Watermelon']
fruits.insert(1, "Orange")  # This will insert like (Inder you want to insert,"What you wana insert")
print(fruits)     
# Output = ['pineapple', 'Orange', 'Banana', 'Coconut', 'Watermelon']
fruits.sort()    # will sort the specified List in alphabetical order
print(fruits) 
# Output= = ['Banana', 'Coconut', 'Orange', 'Watermelon', 'pineapple']
print(fruits.index("Orange"))  # will return the index of specified object in the specified List
# Output = 2
print(fruits.count("Apple"))   # will give a count on how many objects that is specified are in the list
# Output = 0

# SETS:-   {}

numbers = {1,2,3,4,5,6,6}   # Even tho there are 2 6s the set will only have one 6 as its not duplicatable
print(type(numbers))
print(len(numbers))   # will print the length of the set
# output = 6
print("7" in numbers)   # will return a boolean if the object is or not in the list
# Output = False
numbers.add(7) # will add 7 in the set
print(numbers)
# Output = {1, 2, 3, 4, 5, 6, 7}   67 :)
numbers.remove(7) # Will remove specified object from the specified List 
print(numbers)
# Output = {1, 2, 3, 4, 5, 6}  67 :(
numbers.pop() # will pop or remove a object randomly from the set
# Output = it is different every time
numbers.clear()  # clears the set
print(numbers)
# Output = set()

# TUPLE:-  ()

animals = ("Cat","Dog","Rabbit","Lion")
print(type(animals))

print(len(animals))  # Again will just print the length of the tuple
# Output = 4
print("Cat" in animals)  # Again will give a boolean if the specified object is in the specified Tuple
# Output = True
print(animals.index("Dog"))  # Again will give the index of the specified Object in the Specified Tuple
# Output = 1
print(animals.count("Lion"))  # Will count how many of the specified Objects are in the specified Tuple
# Output = 1


# ALso you can use Loops in Tuple as they are iterable
for animal in animals:
    print(animal)
