def isorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
arr = [1,4,3,5,7]
print(isorted(arr))