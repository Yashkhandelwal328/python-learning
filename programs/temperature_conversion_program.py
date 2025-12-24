# C = (F - 32) / (9/5)
# This will ask you if you want to covert Celsius to frahiet or Farahiet to celsius
conversion_from = int(input("Enter 1 : if you want to Celsius to Farahiet\nEnter 2: if you want o convert Farhiet to Celsius\n=> "))
# if it gets input 1 it will convert celcius to farahiet
if conversion_from == 1 :
    celsius_to_farahiet = float(input("Enter Temp in Celcius: "))
    print(f"Converted temp will be {(5/9)*(celsius_to_farahiet)+32}")
# if it gets input 2it will convert Farahiet to Celcius
elif conversion_from == 2 :
    farahiet_to_celcius = float(input("Enter Temp in Farahiet: "))
    print(f"Converted temp will be {(farahiet_to_celcius - 32)/(9/5)}")
# if it gets a invalid i will tell user to enter 1 or 2
else:
    print("please Enter 1 or 2")