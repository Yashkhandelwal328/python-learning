# format specifiers helps to tell f string how the given value should be displayed 
a =1.111
b = 99999999999.999
# by the help of .1f it knew i need 1 float value to be displayed
print(f"{a:.1f}")
# putting :10 will tell it the value to have 10 space used rest will be filled with empty spaces
print(f"{a:10}")
# putting 0 infront of 10 will make it fill empty spaces with 10
print(f"{a:010}")
# to align then we use ^ for center > to right and < to left(default)
print(f"{a:^10}")
# this helps to place a comma after each thousands place
print(f"{b:,}")
# can add multiple of formats by just typing em out
print(f"{b:,.2f}")



