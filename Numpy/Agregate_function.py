import numpy as np

# Aggregate functions = summarize data and typically
#                       return a single value

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.sum(array))
# Output = 55
print(np.mean(array))
# Output = 5.5
print(np.std(array))
# Output = 2.8722813232690143
print(np.var(array))
# Output = 8.25
print(np.min(array))
# Output = 1
print(np.max(array))
# Output = 10
print(np.argmin(array)) # will give the index of minimum value
# Output = 1
print(np.argmax(array))
# Output = 9
print(np.sum(array, axis=0)) # Will sum all coloumns
# Output = [ 7  9 11 13 15]
print(np.sum(array, axis=1)) # Will sum all rows
# Output = [15 40]



