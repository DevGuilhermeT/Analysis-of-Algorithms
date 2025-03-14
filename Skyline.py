def build_max_heap(v, n):
    last_parent = (n-2)//2
    for i in range(last_parent, -1, -1):
        max_heapify(v, i, n)


def max_heapify(v, i, n):
    p = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and v[l][0] > v[p][0]:
        p = l
    if r < n and v[r][0] > v[p][0]:
        p = r
    if p != i:
        v[i], v[p] = v[p], v[i]
        max_heapify(v, p, n)


def heapsort(v, n):
    build_max_heap(v, n)
    for i in range(n-1, 0, -1):
        v[i], v[0] = v[0], v[i]
        max_heapify(v, 0, i)


def skyline(buildings, i, j):
    if j < i:
        return [], 0
    if i == j:
        return [[buildings[i][0], buildings[i][2]], [buildings[i][1], 0]], 2
    mid = (i+j)//2
    l, n_l = skyline(buildings, i, mid)
    r, n_r = skyline(buildings, mid + 1, j)
    return merge(l, r, n_l, n_r)


def merge(l, r, n_l, n_r):
    i, j, pos, h1, h2, x = 0, 0, 0, 0, 0, 0
    ans = [[]]*(n_l + n_r)
    while i < n_l and j < n_r:
        if l[i][0] < r[j][0]:
            x, h1 = l[i]
            i += 1
        elif l[i][0] > r[j][0]:
            x, h2 = r[j]
            j += 1
        else:
            h1 = l[i][1]
            h2 = r[j][1]
            x = r[j][0]
            i += 1
            j += 1
        max_h = max(h1, h2)
        if pos == 0 or (pos != 0 and ans[pos-1][1] != max_h):
            ans[pos] = [x, max_h]
            pos += 1
    while i < n_l:
        if pos == 0 or (pos != 0 and ans[pos-1][1] != l[i][1]):
            ans[pos] = [l[i][0], l[i][1]]
            pos += 1
        i += 1
    while j < n_r:
        if pos == 0 or (pos != 0 and ans[pos-1][1] != r[j][1]):
            ans[pos] = [r[j][0], r[j][1]]
            pos += 1
        j += 1
    return ans, pos


l = [[1, 2, 5], [2, 5, 10], [3, 8, 31], [20, 1, 1], [17, 25, 6], [13, 13, 99]]
heapsort(l, len(l))
print(skyline(l, 0, len(l) - 1))
