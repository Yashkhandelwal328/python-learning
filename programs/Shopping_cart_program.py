# i will make lists and then later append then using for loop
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q": # This is so that even if the user inputs Q it will be converted to q and will exit
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("    ------YOUR CART------")
for i, food in enumerate(foods):     # enumerate helps to run 2 loops in one like this pretty cool ngl
    print(f"{i+1}. {food} (${prices[i]:.2f})")
print()
for price in prices:
    total += price
print(f"Your Total will be ${total:.2f}") 

        
