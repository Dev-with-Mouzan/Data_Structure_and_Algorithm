def quick_sort(A):
    if len(A) <= 1:
        return A
    pivot = A[len(A) // 2]
    left = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    right = [x for x in A if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    A = [3, 6, 8, 10, 1, 2, 1]
    print(quick_sort(A))