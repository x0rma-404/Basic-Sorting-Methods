def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1 

arr = [12, 32, 33, 37, 54, 54, 64, 66, 76, 88, 98]
print(binary_search(arr, 54))  