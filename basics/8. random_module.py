# Random module 
import random

number = random.randint(1,20) # This will get a random number from 1 to 20
print(number)
# Output = 16 , 18 , 7 (so basically random rumber )

number = random.random() # This will print rand float from 0 to 1
print(number)
# Output = 0.2751464742989357

options = ( "rock","paper","scissors" )
option = random.choice(options) # bacically chooses a random option from the collection
print(option)
# Output = scissors (it is random)

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards) # Shuffles the given collection
print(cards)
# Output = ['7', 'J', 'Q', '4', '2', '5', '10', '6', 'K', '3', '8', 'A', '9']