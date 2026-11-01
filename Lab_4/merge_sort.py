def merge_sort(arr):
    # Base Condition
    if len(arr) <= 1:
        return arr

    # Divide Array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursive calls
    merge_sort(left)
    merge_sort(right)

    # Merge sorted halves
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements from Left Array
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements from Right Array
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


n = int(input("Enter the number of elements: "))

arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

print("Sorted Array :.......")
print(merge_sort(arr))
