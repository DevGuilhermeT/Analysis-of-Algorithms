def build_min_heap(v, n):
    last_parent = (n-2)//2
    for i in range(last_parent, -1, -1):
        min_heapify(v, i, n)


def min_heapify(v, i, n):
    p = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and v[l][0] <= v[p][0]:
        if v[l][0] < v[p][0]:
            p = l
        elif v[l][0] == v[p][0] and v[l][1] < v[p][1]:
            p = l
    if r < n and v[r][0] <= v[p][0]:
        if v[r][0] < v[p][0]:
            p = r
        elif v[r][0] == v[p][0] and v[r][1] < v[p][1]:
            p = r
    if p != i:
        v[i], v[p] = v[p], v[i]
        min_heapify(v, p, n)


def heapsort(v, n):
    build_min_heap(v, n)
    for i in range(n-1,0, -1):
        v[i], v[0] = v[0], v[i]
        min_heapify(v, 0, i)


def maximal_points(v, n):
    heapsort(v, n)
    result = [[]]*n
    pos = 0
    max_y = -1000
    for i in range(n):
        if v[i][1] > max_y:
            result[pos] = v[i]
            pos += 1
            max_y = v[i][1]
    return result, pos


lista = [[1,1], [2,2], [2,3], [1,5]]
print(maximal_points(lista, len(lista)))