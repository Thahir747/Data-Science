import numpy as np
row=int(input("Enter the no:of rows:"))
col=int(input("Enter the no:of columns:"))

matrix=[]
print("Enter the values")
for i in range(row):
	a=[]
	for j in range(col):
	  a.append(int(input()))
	matrix.append(a)

print(matrix)


result=np.linalg.inv(matrix)
print("Inverse of the matrix:")
print(result)
