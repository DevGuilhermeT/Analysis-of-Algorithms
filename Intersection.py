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


def binary_search(v, i, j, x):
    mid = i + (j-i)//2
    if j < i:
        return -1
    elif v[mid] == x:
        return mid
    elif v[mid] > x:
        return binary_search(v, i, mid - 1, x)
    else:
        return binary_search(v, mid + 1, j, x)


def intersection_b(n_v, m_v, m):
    heapsort(m_v, m)
    intersection = []
    for number in n_v:
        aux = binary_search(m_v, 0, m - 1, number)
        if aux != -1 :
            intersection.append(m_v[aux])
    return intersection


n = [3, 4, 2, 22, 66, 5]
m = [1, 4, 3, 33]
inter = intersection_b(n, m, len(m))
print(inter)
