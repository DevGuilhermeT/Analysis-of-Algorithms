from math import *


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


def steepest_slope(v, n):
    heapsort(v, n)
    steepest = -inf
    segment = [[]]
    for i in range(1, n):
        if v[i][0] == v[i - 1][0]:
            return [v[i - 1], v[i]]
    for i in range(1, n):
        slope = abs((v[i][1] - v[i - 1][1]) / (v[i][0] - v[i - 1][0]))
        if slope > steepest:
            steepest = slope
            segment = [v[i - 1], v[i]]
    return segment


lista = [[1,2], [2,3], [3,10], [10,11], [2,1]]
print(steepest_slope(lista, len(lista)))