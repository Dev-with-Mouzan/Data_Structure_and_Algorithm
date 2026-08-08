# Sort in ascending order using bubble sort algorithm
def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
if __name__ == "__main__":
    arr1= [64, 34, 25, 12, 22, 11, 90]
    arr2=[23, 45, 12, 67, 34, 89, 1]
    ascending_order = bubble_sort_ascending(arr1)
    desending_order = bubble_sort_descending(arr2)
    print("Sorted array in ascending order is:", ascending_order)
    print("Sorted array in descending order is:", desending_order)
