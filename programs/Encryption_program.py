import random
import string

# chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# or :
chars = " " + string.punctuation + string.digits + string.ascii_letters
# print(chars)
# Output = " !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars = list(chars) # typecasting into a list
key = chars.copy() # This will well copy chars into key
# print(chars) 
# Output = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# print(key)
# Output = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

random.shuffle(key)
# print(key) # randomizes the key
# Output = ['.', '&', '-', 'm', '5', 'D', '>', 'q', '6', 'k', '%', '[', '3', '2', 'W', 'N', '#', 'L', '<', 'h', '$', 'K', "'", '1', 'P', ':', 'E', '?', 'R', 'j', 'X', 'T', 'A', '7', ']', '|', 'C', 'u', 'v', '*', '9', '\\', '0', 'o', 't', ',', '_', 'J', 'F', 'g', 'n', 'B', 'Y', 'G', 'a', 'w', 's', '`', '{', '}', 'd', 'r', 'I', 'M', 'S', '!', 'e', '(', 'O', '=', ')', 'U', 'z', 'f', 'x', 'l', 'y', ' ', '"', 'H', 'Q', '@', '+', '^', '/', 'c', '8', ';', 'V', '~', 'b', 'Z', '4', 'p', 'i']


meow = input("Enter 1 --> Encrypt\n      2 --> Decrypt\n      =>")
# Encryption :-
if meow == '1':
    plain_text = input("Enter a message to encrypt: ") # This will be the input
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"orignal message: {plain_text}")
    print(f"encrypted message: {cipher_text}")

# Decryption :-
elif meow == '2':
    cipher_text = input("Enter a message to encrypt: ") # This will be the input
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"encrypted message: {cipher_text}")
    print(f"orignal message: {plain_text}")
else:
    print("Enter a valid response")