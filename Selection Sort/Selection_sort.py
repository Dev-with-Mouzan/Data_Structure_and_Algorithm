def Selection_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def Selection_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
# Example usage
if __name__ == "__main__":
    arr1 = [64, 25, 12, 22, 11]
    arr2 = [23, 45, 12, 67, 34]
    ascending_order = Selection_sort_ascending(arr1)
    desending_order = Selection_sort_descending(arr2)
    print("Sorted array in ascending order is:", ascending_order)
    print("Sorted array in descending order is:", desending_order)