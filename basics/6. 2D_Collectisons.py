fruits =     ["apple","orange","banana","coconut"]
vegetables = ["celery","carrot","potatoes"]
meats =      ["chicken","fish","turkey"]
              
groceries = [fruits,vegetables,meats]

# we can also just do this instead
# groceries = [
#     ["apple","orange","banana","coconut"]
#     ["celery","carrot","potatoes"]
#     ["chicken","fish","turkey"]
# ]

print(groceries) # This will print out all lists sepearted by a ','
# Output = [['apple', 'orange', 'banana', 'coconut'], ['celery', 'carrot', 'potatoes'], ['chicken', 'fish', 'turkey']]
print(groceries[0]) # This will print out groceries at index 0 
# Output = ['apple', 'orange', 'banana', 'coconut']
print(groceries[0][1]) # This will print out the 2d_list's sepecified index's specified object
# Output = orange 

for collection in groceries:
    print(collection)
# Output = ['apple', 'orange', 'banana', 'coconut']
#          ['celery', 'carrot', 'potatoes']
#          ['chicken', 'fish', 'turkey']
for collection in groceries:
    for food in collection:
        print(food)
# Output = orange
        #   apple
        #   orange
        #   banana
        #   coconut
        #   celery
        #   carrot
        #   potatoes
        #   chicken
        #   fish
        #   turkey

for collection in groceries:
    for food in collection:
        print(food, end =" ")
# apple orange banana coconut celery carrot potatoes chicken fish turkey

print()

# Trying to make a numpad

numpad = (('1','2','3'),
          ('4','5','6'),
          ('7','8','9'),
          ('*','0','#'))

for i in numpad:
    for j in i:
        print(j,end =" ")
    print()                           # This will print a extra line after each tuple so it formats correctly
# Output =  1 2 3
#           4 5 6
#           7 8 9
#           * 0 #