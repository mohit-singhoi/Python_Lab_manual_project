#Q.5 Use NumPy for array operations

import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([100, 200, 300, 400, 500])

# #Arithmetic Operation
# print("Sum :",a+b)
# print("Sub :",a-b)
# print("Mul :",a*b)
# print("Div :",b/a)
# print("Mod :",a%b)
# print("Power :",a**2)


# #Mathematical Function
# print(np.sqrt(a))
# print(np.exp(a))
# print(np.log(a))
# print(np.sin(a))


# #Aggregate Function
# print(a.sum())     # 15
# print(a.mean())    # 3.0
# print(a.max())     # 5
# print(a.min())     # 1
# print(a.std())     # Standard deviation


# #Matrix Operation
# A= np.array([[1,2],[3,4]])
# B=np.array([[5,10],[15,20]])


# print("Sum :",A+B)
# print("Sub :",A-B)
# print("Mul :",A*B)
# print("Transpose :",A.T)
# print("Multiplication : ",np.dot(A,B))


#Conditional Operations
print(a > 2)         
print(a[a > 2])     
print(np.where(a%2==0, "Even", "Odd"))
['Even' 'Even' 'Even' 'Even' 'Even']


