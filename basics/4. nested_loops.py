# nested loops = A loop within another loop (outer,inner)
#          outer_loop: 
#              inner_loop:


for i in range(3):    # this will loop the inner loop 3 times
    for j in range(1,11):     # the counter for inner_loop should be different
        print(j,end = " ")    # the end is by default set to \n we made it have a space so all of loop will be printed in one line 
    print()    # This is to print a new line after every inner loop is completed    
    