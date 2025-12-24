import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]
                ])

# array[start:end:step] end is not inclusive by default step is 1

print(array[0:3:2])
#  Output = [[ 1  2  3  4]
#            [ 9 10 11 12]]
print(array[::-1])
# Output = [[13 14 15 16]
#           [ 9 10 11 12]
#           [ 5  6  7  8]
#           [ 1  2  3  4]]

# Now if you want to do this with coloumns:-

print(array[:,0:3:2]) 
# Output = [[ 1  3]
#           [ 5  7]
#           [ 9 11]
#           [13 15]]

print(array[0:2,2:])
# Output = [[3 4]
#           [7 8]]