# 1 pound = 0.453592
# this is to get input on whether user wants to convert from pound to weight or weight to pound
conversion_from = int(input("Enter 1 : if you want to convert pound to Kilogram\nEnter 2 : if you want to convert Kilogram to pound\n=> "))
# if we recive 1 it will convert pounds to kilogram 
if conversion_from == 1 :
    pounds_to_kilogram = float(input("Enter weight in pounds: "))
    print(f"{pounds_to_kilogram}pounds will be {pounds_to_kilogram*0.453592} Kilograms")
# if we recive 2 it will convert kilograms to pounds
elif conversion_from == 2 :
    kilograms_to_pounds = float(input("Enter weight in kilograms: "))
    print(f"{kilograms_to_pounds} kilograms will be {kilograms_to_pounds/0.453592} pounds")
# if we recive anything else it will tell user to give a valid command
else:
    print("please put a value from 1 or 2")