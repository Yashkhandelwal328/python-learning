import numpy as np

# Broadcasting allows Numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.

# For braodcasting both rows and columns must :-
# The dimensions have the same size
# OR
# One of the dimensions has a size of 1.

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],
                   [2],
                   [3],
                   [4]])
print(array1.shape) # Output = (1, 4)
print(array2.shape) # Output = (4, 1) 
# As one of then is 1 they will work as both rows and coloumns has a one

array3 = array1 * array2
print(array3)
# Output = [[ 1  2  3  4]
#           [ 2  4  6  8]
#           [ 3  6  9 12]
#           [ 4  8 12 16]]

print(array3.shape) # Output = (4, 4)

# array1 = np.array([[1,2,3,4],
#                    [5,6,7,8]])
# array2 = np.array([[1],
#                    [2],
#                    [3],
#                    [4]]) 
# Here with (2, 4) 
#           (4, 1)
# there is no one in rows and also no dimensions are same

# array3 = array1 * array2
# print(array3)
# Output =  File "c:\Users\yashi\OneDrive\Documents\meowmeow\Numpy\Broadcasting.py", line 36, in <module>
#     array3 = array1 * array2
#              ~~~~~~~^~~~~~~~
# ValueError: operands could not be broadcast together with shapes (2,4) (4,1)

# array3 = array1 + array2
# Output =   File "c:\Users\yashi\OneDrive\Documents\meowmeow\Numpy\Broadcasting.py", line 43, in <module>
#    array3 = array1 + array2
#             ~~~~~~~^~~~~~~~
#ValueError: operands could not be broadcast together with shapes (2,4) (4,1)

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array1.shape) # Output = (1, 10)
print(array2.shape) # Output = (10, 1)

array3 = array1 * array2
print(array3)
# Output = [[  1   2   3   4   5   6   7   8   9  10]
#           [  2   4   6   8  10  12  14  16  18  20]
#           [  3   6   9  12  15  18  21  24  27  30]
#           [  4   8  12  16  20  24  28  32  36  40]
#           [  5  10  15  20  25  30  35  40  45  50]
#           [  6  12  18  24  30  36  42  48  54  60]
#           [  7  14  21  28  35  42  49  56  63  70]
#           [  8  16  24  32  40  48  56  64  72  80]
#           [  9  18  27  36  45  54  63  72  81  90]
#           [ 10  20  30  40  50  60  70  80  90 100]]
print(array3.shape) # Output = (10, 10)
