import array


arr= array.array("i",[1,2,3,4,5,6])

# check type code of the array
print("Type code of the array: ",arr.typecode)

# check length of the array
print("Length of the array: ",len(arr))

# check item size of the array
print("Item size of the array: ",arr.itemsize)

# check buffer information of the array
print("Buffer information of the array: ",arr.buffer_info())



# check bytes of the array
print("Bytes of the array: ",arr.tobytes())

# reverse the array
rev_array=arr.reverse() 
print("Reversed array: ",rev_array)


# insert an element in the array
arr.insert(2,7)
print("Eelment in the array after insertion: ",end=" ")
for i in arr:
    print(i,end=" ")


# remove an element from the array
arr.remove(7)
print("\nEelment in the array after removal: ",end=" ")
for i in arr:
    print(i,end=" ")


# pop an element from the array
arr.pop(2)
print("\nEelment in the array after pop: ",end=" ")
for i in arr:
    print(i,end=" ")


# append an element in the array
arr.append(8)
print("\nEelment in the array after append: ",end=" ")
for i in arr:
    print(i,end=" ")


# extend an element in the array
arr.extend([9,10])
print("\nEelment in the array after extend: ",end=" ")
for i in arr:
    print(i,end=" ")

# copy an element in the array
arr1=arr
print("\nEelment in the array after copy: ",end=" ")
for i in arr1:
    print(i,end=" ")

# count an element in the array
print("\nCount of 5 in the array: ",arr.count(5))


# index an element in the array
print("Index of 5 in the array: ",arr.index(5))

# slicing of array
print("Eelment in the array after slicing: ",end=" ")
for i in arr[1:4]:
    print(i,end=" ")

# reverse slicing of array
print("\nEelment in the array after reverse slicing: ",end=" ")
for i in arr[::-1]:
    print(i,end=" ")


