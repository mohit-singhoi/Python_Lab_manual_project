#Q.6 Use NumPy for indexing and slicing

import numpy as np


# # Creating 1D Array
# arr = np.array([10,20,30,40,50,60])
# print(arr) 

# #indexing
# print(arr[0])
# print(arr[-1])
# print(arr[2])


# # Slicing
# print(arr[1:4])
# print(arr[:3])
# print(arr[3:])
# print(arr[::2])
# print(arr[::-1])


# Creating 2D Array
arr2d= np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

#Indexing of 2D Array

print(arr2d[0, 0])   # 1
print(arr2d[1, 2])   # 6
print(arr2d[-1, -1]) # 9

#Slicing of 2D Array
print(arr2d[0:2, 1:3]) 
print(arr2d[:, 0])
print(arr2d[1, :]) 
print(arr2d[:, ::2])