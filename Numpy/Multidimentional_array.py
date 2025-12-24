import numpy as np 

array0 = np.array('A') # only has one elemnt one dot 0 dimentions

print(array0.ndim) # this will print number of diemntions
# Output = 0
array1 = np.array(['A','B','C'])
print(array1.ndim)
# Outpuy = 1
array2 = np.array([['A','B','C'], # This is a 2d array (2 diemtional)
                   ['D','E','F'], # also refred as matrix
                   ['G','H','I']] # as it has rows and coloumns
                ) 
print(array2.ndim)  
# Output = 2
# array3 = np.array(
#     ([[['A','B','C'],['D','E','F'],['G','H','I']],
#     [['J','K''L'],['M','N','O'],['P','Q','R']],
#     [['S','T','U'],['V','W','X'],['Y','Z']]])
# )
# print(array3.ndim)
# Output = ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 2 dimensions. The detected shape was (3, 3) + inhomogeneous part.
# so you need to fill the last one 
array3 = np.array(
    ([[['A','B','C'],['D','E','F'],['G','H','I']],
    [['J','K','L'],['M','N','O'],['P','Q','R']],
    [['S','T','U'],['V','W','X'],['Y','Z',' ']]])
)
print(array3.ndim)
# Output = 3
print(array3.shape) # This will return (depth,Rows,Columns)
# Output = (3, 3, 3)
print(array2.shape)
# Output = (3, 3)

# To access the value in normal python we do chain indexing like : - 
print(array3[0][0][0])
# Output = A
# But with numpy we can do MULIDIMENTIONAL INDEXING it is faster than chain indexing 
print(array3[0,2,1])
# Output = H

# trying to print my name :3
name = array3[2,2,0] + array3[0,0,0] + array3[2,0,0] + array3[0,2,1]
print(name)
# Output = YASH