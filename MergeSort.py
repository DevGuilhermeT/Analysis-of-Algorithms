def intercalate(array, start, mid, end):
    aux1 = []
    aux2 = []
    global ans
    for i in range(start, mid + 1):
        aux1.append(array[i])
    for i in range(mid+1, end + 1):
        aux2.append(array[i])
    i = 0
    j = 0
    k = start
    while i < mid-start+1 and j < end-mid:
        if aux1[i] <= aux2[j]:
            array[k] = aux1[i]
            i = i + 1
        else:
            array[k] = aux2[j]
            ans[0] += (len(aux1)-i)
            j = j + 1
        k = k + 1
    while i < mid-start+1:
        array[k] = aux1[i]
        i = i + 1
        k = k + 1
    while j < end-mid:
        array[k] = aux2[j]
        j = j + 1
        k = k + 1


def merge_sort(array, i, j):
    if i < j:
        mid = (i+j)//2
        merge_sort(array, i, mid)
        merge_sort(array, mid+1, j)
        intercalate(array, i, mid, j)


ans = [0]
v = [1,2,3,4,5,6,7,5,4,3,6,7,5,4,3]
merge_sort(v, 0, len(v)-1)
print(ans)
