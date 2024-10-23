def mergeLists(list_a, list_b):
    res = []
    pointer_a, pointer_b = 0, 0
    while pointer_a < len(list_a) and pointer_b < len(list_b):
        if list_a[pointer_a] < list_b[pointer_b]:
            res.append(list_a[pointer_a])
            pointer_a += 1
        elif list_b[pointer_b] < list_a[pointer_a]:
            res.append(list_b[pointer_b])
            pointer_b += 1
    while pointer_a < len(list_a):
        res.append(list_a[pointer_a])
        pointer_a += 1
    while pointer_b < len(list_b):
        res.append(list_b[pointer_b])
        pointer_b += 1
    print(res)
            



list_a = [1,3,5,7,9]
list_b = [2,4,6,8,10,12,14]
mergeLists(list_a,list_b)