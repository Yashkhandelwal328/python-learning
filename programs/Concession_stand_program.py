menu = {
        "pizza":3.0,
        "nachos":4.5,
        "popcorn":6.0,
        "fries":2.5,
        "chips":1.0,
        "pretzel":3.5,
        "soda":3.0,
        "lemonade":4.25
        }

cart = []
total = 0

print("     --------------------MENU--------------------     ")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("     ---------------------------------------------    ")
while True:
    cart_input = input("Enter what do you want to get into your cart (press q to quit): ").lower()
    if cart_input == "q" :
        break
    elif menu.get(cart_input):
        cart.append(cart_input)
        total += menu.get(cart_input)
    else:   
        print(f"Sorry we yet dont have {cart_input} in our store")

print("     --------------------CART--------------------     ")
for j,i in enumerate(cart):
    print(f"{j+1}. {i}")
print("     --------------------TOTAL--------------------    ")
print(f"Total : ${total:.2f}")
print("     ---------------------------------------------    ")


