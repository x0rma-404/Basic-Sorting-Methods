def buble(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr = [64,32,76,98,54,54,33,88,66,12,37]
print(buble(arr))