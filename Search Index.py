def build_max_heap(v, n):
    last_parent = (n-2)//2
    for i in range(last_parent, -1, -1):
        max_heapify(v, i, n)


def max_heapify(v, i, n):
    p = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and v[l] > v[p]:
        p = l
    if r < n and v[r] > v[p]:
        p = r
    if p != i:
        v[i], v[p] = v[p], v[i]
        max_heapify(v, p, n)


def heapsort(v, n):
    build_max_heap(v, n)
    for i in range(n-1, 0, -1):
        v[i], v[0] = v[0], v[i]
        max_heapify(v, 0, i)


def high_binary_search(v, i, j, x, n):
    mid = i + (j-i)//2
    if j < i:
        return -1
    elif v[mid] == x:
        if (mid+1) < n:
            if v[mid + 1] == x:
                return high_binary_search(v, mid + 1, j, x, n)
        return mid
    elif v[mid] > x:
        return high_binary_search(v, i, mid - 1, x, n)
    else:
        return high_binary_search(v, mid + 1, j, x, n)


def low_binary_search(v, i, j, x, n):
    mid = i + (j-i)//2
    if j < i:
        return -1
    elif v[mid] == x:
        if (mid-1) >= 0:
            if v[mid - 1] == x:
                return low_binary_search(v, i, mid - 1, x, n)
        return mid
    elif v[mid] > x:
        return low_binary_search(v, i, mid - 1, x, n)
    else:
        return low_binary_search(v, mid + 1, j, x, n)


def create_v(v, n):
    vector = []
    for i in range(0, n):
        x, y = v[i]
        for j in range(x, y+1):
            vector.append(j)
    heapsort(vector, len(vector))
    return vector


def search_index(v, n, x):
    vector = create_v(v, len(v))
    aux = [0]*2
    aux[0] = low_binary_search(vector, 0, len(vector) - 1, x, len(vector))
    aux[1] = high_binary_search(vector, 0, len(vector) - 1, x, len(vector))
    return aux


vector = [(1, 3), (7, 9), (1, 8)]
interval = search_index(vector, len(vector), 7)
print(interval)
