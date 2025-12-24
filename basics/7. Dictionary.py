# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"
            }
 
# Dict meathods

# here USA is the key and Washington D.C. is the value 
print(capitals.get("USA")) # with get we can get the value using the key print(dict.get("key"))
# Output = Washington D.C.
print(capitals.get("Japan")) # Japan is not in the dictionary it will print none
# Output = None
if capitals.get("Russia"): # This is used to quicly check if the key exists or not
    print("Exists")
else :
    print("nuuh")  
# Output = Exists

capitals.update({"Germany":"Berlin"}) # Update helps to add or update key value pairs
print(capitals)
# Output = {'USA': 'Washington D.C.', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}
# we can also use this to update like:
capitals.update({"USA":"Berlin"}) 
print(capitals)
# Output = {'USA': 'Berlin', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}

capitals.pop("China") # We can pop or remove a key value pair from a dict by giving it the key like dict.pop("key")
print(capitals)
# Output {'USA': 'Berlin', 'India': 'New Delhi', 'Russia': 'Moscow', 'Germany': 'Berlin'}

capitals.popitem() # it will remove the latest key iten that was inserted
print(capitals)
# {'USA': 'Berlin', 'India': 'New Delhi', 'Russia': 'Moscow'}

# capitals.clear() # will clear the dict
# print(capitals)
# # Output = {}

keys = capitals.keys() # now 'keys' will have all keys listed

print(keys)
# Output = dict_keys(['USA', 'India', 'Russia'])

values = capitals.values()   # gives values that recembles a list
print(values)
# Output = dict_values(['Berlin', 'New Delhi', 'Moscow'])
for i  ,value in enumerate(capitals.values()):
    print(f"{i + 1}. {value}")
# Output = 1. Berlin
#          2. New Delhi
#          3. Moscow

items = capitals.items() # items = [(),(),()]
print(items) 
# Output = dict_items([('USA', 'Berlin'), ('India', 'New Delhi'), ('Russia', 'Moscow')])

# items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")
# Output = USA: Berlin
#          India: New Delhi
#          Russia: Moscow

