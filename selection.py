def selection(arr):
    n = len(arr)
    for i in range(n):
        pivot = i
        for j in range (i+1,n):
            if arr[pivot] > arr[j]:
                pivot = j
        arr[pivot],arr[i] = arr[i],arr[pivot]
    return arr

arr = [64,32,76,98,54,54,33,88,66,12,37]
print(selection(arr))