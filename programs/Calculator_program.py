# this is to take input on what operttor to take
a = input("Enter an opertator (+ - * /): ")
a1 = int(input("Enter the 1st number: "))
a2 = int(input("Enter the 2nd number: "))
if a == '+':
   b =  a1 + a2 
elif a == "-":
   b =  a1 - a2
elif a == "*":
   b =  a1 * a2 
else:
   b = a1 / a2 
print(b)