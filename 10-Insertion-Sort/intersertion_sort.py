def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    arr1 = [23,45,67,89,4,2]
    #print first array
    print(insertion_sort(arr))

    # print second array
    print(insertion_sort(arr1))