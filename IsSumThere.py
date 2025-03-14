def intercalate(array, start, mid, end):
    aux1 = []
    aux2 = []
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


def binary_search(v, start, end, x):
    if end >= start:
        mid = start+(end - start)//2
        if v[mid] == x:
            return True
        elif v[mid] > x:
            return binary_search(v, start, mid - 1, x)
        else:
            return binary_search(v, mid + 1, end, x)
    else:
        return False


def is_sun_there(a1, a2, x):
    merge_sort(a2, 0, len(a2) - 1)
    for i in a1:
        aux = x - i
        if binary_search(a2, 0, len(a2)-1, aux):
            return True
    return False


ans = []
v1 = [12, 11, 13, 5, 6, 7]
v2 = [3, 7, 9, 12, 82, 86]
print(is_sun_there(v1, v2, 21))
