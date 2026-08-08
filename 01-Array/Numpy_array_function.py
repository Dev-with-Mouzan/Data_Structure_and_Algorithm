import numpy as np

arr= np.array([1,2,3,4,5,6])

print("Type code of the array: ",arr.dtype)

print("Length of the array: ",len(arr))

print("Item size of the array: ",arr.itemsize)

print("Buffer information of the array: ",arr.data)

# 2 diemensional array
print("2 diemensional array:",end=" ")
arr= np.array([[1,2,3],[4,5,6]])
for i in arr:
    print(i)


# 3 diemensional array
print("\n3 diemensional array:",end=" ")
arr= np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
for i in arr:
    print(i)

# All other function of numpy are already placed in the Numpy repository kindly visit it for complete information of numpy