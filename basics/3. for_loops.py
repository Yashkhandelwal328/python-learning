# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string,sequence, etc.

for i in range(1,11,2):         # (start,end,step) the end one is exclusive
    print(i)

for i in reversed(range(1,11,2)):            # reversed function will reverse the order it will be printed 
    print(i)  



# we can also print a string in a line like this :-
# y
# a
# s
# h

string = "Yash Meow"
for i in string:
    print(i)

for i in range(1,21):
    if i == 5:
        continue      # This will pass when i is 5 and continue afterwards
    else :
        print(i)
for i in range (1,21):
    if i == 8:
        break        # This will stop the loop if i is equals to 8
    else :
        print(i)
        # Six Seven


