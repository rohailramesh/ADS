def removeElement(arr,target):
    k = 0
    for i in range(len(arr)):
        if arr[i] != target:
            print(arr[i])
            arr[k] = arr[i]
            k +=1
    return k

arr = [3,5,1,2,1,9]
target = 1
print(removeElement(arr,target))