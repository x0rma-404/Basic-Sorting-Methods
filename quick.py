def quick(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = []
    right = []
    middle = []
    
    for i in arr:
        if i == pivot:
            middle.append(i)
        elif i < pivot:
            left.append(i)
        else:
            right.append(i)
        
    return quick(left) + middle + quick(right)

arr = [64,32,76,98,54,54,33,88,66,12,37]
print(quick(arr))