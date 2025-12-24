# # we will use a lib name time by using import
# import time

# my_time = int(input("Enter the time in seconds: "))

# for i in range(my_time,0,-1):    # we are just repeating time.sleep so it appears like a times while also printing a countdown
#     print(i)
#     time.sleep(1)      # time.sleep will cause a countdown till program closes

# print("TIMES'S UP")


# now lets add minutes and hours and make it a digital clock



# we will use a lib name time by using import
import time

my_time = int(input("Enter the time in seconds: "))

for i in range(my_time,0,-1):    # we are just repeating time.sleep so it appears like a times while also printing a countdown
    seconds = i % 60    # this will make it so seconds cant go above 60 as there are 60 seconds in a minute
    minutes = int((i / 60) % 60)     #  '/' is used cuz we want minutes to count after seconds and '%' cuz there are 60 minutes
    hours = int(i / 3600)        # cuz there are 3600 seconds in an hour
    print(f"{hours:02}:{minutes:02}:{seconds:02}")    # format specifiers to allow then to have 2 spaces with 0 padding too       
    time.sleep(1)      # time.sleep will cause a countdown till program closes

print("TIMES'S UP")