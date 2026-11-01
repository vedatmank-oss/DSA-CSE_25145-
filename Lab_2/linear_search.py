def lin_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"{key} at index {i}")
            return
    print(f"{key} not found")


n = int(input("Enter the number of elements: "))

arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the key: "))

result = lin_search(arr, key)
