def quicksort(a,low,high):
    if low < high:
        i = low
        j = high
        pivot = low
        while i < j:
            while i < len(a) and a[i] <= a[pivot]:
                i+=1
            while a[j] > a[pivot]:
                j-=1
            if i < j:
                a[i],a[j] = a[j],a[i]
        a[j],a[pivot] = a[pivot],a[j]
        quicksort(a,low,j-1)#Left Part
        quicksort(a,j+1,high)#Right Part

#Entering the Elements
n = int(input("Enter the number of elements: "))
a = []

print("Enter elements:")
for i in range(n):
    a.append(int(input()))

quicksort(a, 0, n - 1)

print("Sorted Array :.......")
print(a)