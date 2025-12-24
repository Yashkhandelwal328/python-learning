import numpy as np

# Scalar arithmetic

array = np.array([1,2,3])

print(array + 1)
# Output = [2 3 4]
print(array-2)
# Output = [-1  0  1]
print(array * 3)
# Output = [3 6 9]
print(array/4)
# Output = [0.25 0.5  0.75]
print(array ** 5)
# Output = [  1  32 243]

print(np.sqrt(array))
# Output = [1.         1.41421356 1.73205081]

array1 = np.array([1.01,2.5,3.99])
print(np.round(array1)) # to always round down use floor , to always round up use ceil
# Output = [1. 2. 4.]

# Exercise:-
radii = np.array([1,2,3])
area = (radii**2)*np.pi
print(area)
# Output = [ 3.14159265 12.56637061 28.27433388]

# Element-wise arithmetic :-

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
# Output = [5 7 9]

print(array1 - array2)
# Output = [-3 -3 -3]

print(array1 * array2)
# Output = [ 4 10 18]

print(array1 / array2)
# Output = [0.25 0.4  0.5 ]

print(array1 ** array2)
# Output = [  1  32 729]

# Comparison Operators :-

scores = np.array([91,55,100,73,82,64])

print(scores == 100) # This will return a boolean if any score is equals to 100
# Output = [False False  True False False False]

scores[scores < 60] = 0
print(scores)
# Output = [ 91   0 100  73  82  64]
