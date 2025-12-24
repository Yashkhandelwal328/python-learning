import numpy as np
import tkinter as tk
# # *
# # **
# # ***
# # ****
# # *****
# a = ""
# for i in range(5):
#     a = a + "*"
#     print(a)

# #     * 1
# #    *** 3
# #   ***** 5
# #  ******* 7
# # ********* 9
# rows = 5
# for i in range(1,rows+1):
#     print(" " * (rows - i) + "*" * (2*i - 1) )

# for i in range(1,51):
#     print(i)

# list = []
# for i in range(1,101):
#     list.append(i)

# print(sum(list))

# a = "*"
# for i in range(1,6):
#     print(a * i)

# for i in range(2,101):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue


# for i in range(1,11):
#     print(f"7 X {i} = {7*i}")

# str = "kawaii"
# vowels = []
# consonants = []
# for i in str:
#     if i in "aeiou":
#         vowels.append(i)
#     else:
#         consonants.append(i)

# print(f"total vowels = {len(vowels)}")
# print(f"total consonants = {len(consonants)}")

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i + 1):
#         print(j, end = "")
#     print()

# str = "kawaii"
# rev_str = ""
# for i in str:
#     rev_str =  i + rev_str
# print(rev_str)

# list = [1, 10 ,5 , 4]
# max = list[0]
# for i in list:
#     if max >= i:
#          continue
#     else:
#          max = i 
# print(max)
         
import math

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     limit = int(math.sqrt(n)) + 1
#     for i in range(3, limit, 2):
#         if n % i == 0:
#             return False
#     return True

# # test it
# for x in [1, 2, 3, 4, 5, 9, 11, 25, 29]:
#     print(x, "->", is_prime(x))

#     *
#    ***
#   *****
#  *******
# *********

# for i in range(1,6):
#     print(" " * (5-i) + "*" * (2*i - 1))

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# for i in range(1,6):
#     print(" " * (5-i) + "*" * (2*i - 1))
# for i in range(1,5):
#     print(" " * (i) + "*" * ((10 - 2*i - 1)))

# num = "5621"
# l1 = []
# for i in num:
#     l1.append(int(i))

# print(sum(l1))

def sum_loop():
    num = input("Enter a number:")
    l1 = []
    for i in num:
        l1.append(int(i))
    return(sum(l1))

# print(sum_loop())

def rep_char():
    word = input("Enter a word")
    l1 = []
    for i in word:
        if i == "g":
            l1.append(i)
        else:
            continue
    print(f"g -->{len(l1)}")

# rep_char()

def char_freq(word):
    freq = {}
    for i in word:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for key, value in freq.items():
        print(f"{key} --> {value}")

# char_freq("programming")

def palindrom_check(word):
    l1 = []
    l2 = []
    for i in word:
        l1.append(i)
    for j in reversed(word):
        l2.append(j)
    if l1 == l2:
        print(f"yes the {word} is palindrome")
    else:
        print(f"sadly {word} is not plaindrome") 

# palindrom_check("racecar")

def fibonacci_sequence(n):
    a = 0
    b = 1

    print(a, b, end=" ")

    for i in range(n - 2):
        next = a + b
        print(next , end=" ")
        a = b
        b = next

# fibonacci_sequence(10)



def list_strip(l1):
    l1_striped = []
    for i in l1:
        if i in l1_striped:
            continue
        else:
            l1_striped.append(i)
    print(l1_striped)

# list_strip([1, 2, 2, 3, 3, 3, 4])

def list_freq(l1):
    freq= {}
    for i in l1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for key, value in freq.items():
        print(f"{key}--> {value}")

# list_freq([1, 2, 2, 3, 3, 3, 4])

# l1 = [1, 2, 2, 3, 3, 3, 4]

# l1 = l1[::-1]
# print(l1)

# def l1():
#     l1 = l1[::-1]

def reversed_list(l1):
    n = len(l1)
    for i in range(n//2):
        l1[i], l1[n - 1 - i] = l1[n - 1 - i], l1[i]
    return l1
    
# print(reversed_list([1, 2, 2, 3, 3, 3, 4]))

def perfect(n):
    if n <=1 :
        return "not perfect"
    else:
        total = 0
        for i in range(1,n//2+1):
            if n % i == 0:
                total += i
            else:
                continue
    if total == n :
        return "perfect"
    else :
        return "not perfect"

# print(perfect(28))

def get_evens(lst):
    even_lst = []
    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            continue
    return even_lst

# print(get_evens([1, 2, 2, 3, 3, 3, 4]))

def get_min_max(lst):
    max = lst[0]
    min = lst[0]
    for i in lst:
        if max >= i:
            continue
        else:
            max = i
    for i in lst:
        if min <= i:
            continue
        else:
            min = i
    return (min,max)

# print(get_min_max([5, 1, 9, 3]))

def even_np(a):
    even = a[a % 2 == 0]
    return even

# print(even_np(np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])))

# arr = np.array([10, 20, 30, 40, 50])
# print(arr[2:])

# arr = np.array(
#     ([[['A','B','C'],['D','E','F'],['G','H','I']],
#     [['J','K','L'],['M','N','O'],['P','Q','R']],
#     [['S','T','U'],['V','W','X'],['Y','Z',' ']]])
# )
# print(arr[1,1,0])

# arr = np.array([[2, 4, 6],
#                 [1, 3, 5],
#                 [7, 9, 11]])
# print(arr[:,0])
# print(arr[2:])

# arr1 = np.array([[5, 6, 7],
#                 [8, 9, 10]])

# arr2 = np.array([1,2,3])

# print(arr1 + arr2)

# arr = np.array([[3, 9, 12],
#                 [6, 18, 24],
#                 [15, 30, 45]])
# print(np.mean(arr, axis= 0))
# print(np.mean(arr, axis= 1))

# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])

# print(arr[0,0,]+ arr[1,1] + arr[2,2])


# 2.Design a simple GUI application using Tkinter that takes user input for their name and displays a greeting message.

# import pyaudio

# pa = pyaudio.PyAudio()

# print("Device count:", pa.get_device_count())
# for i in range(pa.get_device_count()):
#     info = pa.get_device_info_by_index(i)
#     print(i, info.get('name'), "| inputs:", info.get('maxInputChannels'))


# import numpy as np
# a = np.array([[1,2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# print(np.concatenate([a, b]))

# y = 6
# z = lambda x: x * y
# print(z(8))


def factorial(n):
    if n == 1 or 0:
        return 1
    else :
        return n*factorial(n-1)

# print(factorial(20))



def prime(n):
    if n <=1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(n**0.5) + 1
    for i in range(1,limit,3):
        if n % i ==0:
            return False
        return True
    
# print(prime(7))




def fac(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n*fac(n-1)
    
# print(fac(0))

# import numpy as np
# a = np.array([[1,2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# print(np.concatenate([a, b]))

def sum_num(n):
    l1 = []
    n = str(n)
    for i in n:
        i = int(i)
        l1.append(i)
    return sum(l1)

# print(sum_num(875386946))

def sum_N(N):
    l1 = []
    for i in range(N+1):
        l1.append(i)
    return sum(l1)
    # sum = 0
    # i=0
    # while i<=N:
    #     sum += i
    #     i+= 1
    # return sum


# print(sum_N(3))

# L = [1, 2, 3]
# def incr(x):
#  return x+1
# print(list(map(incr, L)))

# str = "kawaii"
# rev_str = ""
# for i in str:
#     rev_str =  i + rev_str
# print(rev_str)

def largest(l1):
    largest = []
    for i in l1:
        if largest == []:
            largest.append(i)
        elif largest[0] <= i :
            largest.pop(0)
            largest.append(i)
        else:
            continue
    return largest[0]

# print(largest([1,2,9,2]))


def sum_num(n):
    l1 = []
    n = str(n)
    for i in n:
        i = int(i)
        l1.append(i)
    return sum(l1)


n = 9876536
l1 = []
n = str(n)
for i in n:
    i = int(i)
    l1.append(i)

# print(sum(l1))

def removekth(s,k):
    if k>= len(s):
        return s
    else:
        return s[:k] + s[k+1:]

# print(removekth("kawaii",1))

# for i in range(10):
    # print(" " * (10-i) + "*" * (2*i-1))


# import turtle
# t = turtle.Turtle()
# # t.penup()
# # t.goto(100,10)
# # t.pendown()
# for i in range(3):
#     t.forward(100)
#     t.left(120)

n= int(input())
for i in range(2,n):
    if n%i==0:
        print("not prime")
        continue
    else:
        print("prime")
        break