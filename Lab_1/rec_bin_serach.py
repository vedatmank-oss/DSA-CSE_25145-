def rec_bin_search(arr,key,low,high):
    if low > high :
        return -1
    mid = (low+high)//2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return rec_bin_search(arr,key,low,mid-1)
    else:
        return rec_bin_search(arr,key,mid+1,high)

Emp_Ids = [1002, 1005, 1012, 1025, 1040, 1077, 1100]
search_id = int(input("Enter Employee ID to search: "))

result_index = rec_bin_search(Emp_Ids,search_id,0,(len(Emp_Ids)-1))
if result_index != -1:
    print(f"Employee ID {search_id} found at index {result_index}.")
else:
    print(f"Employee ID {search_id} not found in the HR system.")