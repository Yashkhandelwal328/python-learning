import numpy as np

my_list = [1,2,3,4]

my_list = my_list * 2 # It will just repeat it

print(my_list)
# Output = [1, 2, 3, 4, 1, 2, 3, 4]

# numpy arrys are superior then normal list cuz its fater and better

array = np.array([1,2,3,4])
print(array)
# Output = [1 2 3 4]
print(type(array))
# Output = <class 'numpy.ndarray'>

array = array * 2 
print(array)
# Output = [2 4 6 8]