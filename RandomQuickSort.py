from random import randint


def partition(v, l, r):
    p_i = randint(l, r)
    v[p_i], v[l] = v[l], v[p_i]
    p = v[l]
    i = l
    j = r
    while i < j:
        while i < r and v[i] <= p:
            i += 1
        while j > l and v[j] > p:
            j -= 1
        if i < j:
            v[i], v[j] = v[j], v[i]
    pos = j
    v[l], v[pos] = v[pos], v[l]
    return pos


def quick_sort(v, l, r):
    if l < r:
        pos = partition(v, l, r)
        quick_sort(v, l, pos - 1)
        quick_sort(v, pos + 1, r)


v = [12, 123, 44, 55123, 53, 66, 13, 52]
n = len(v)
quick_sort(v, 0, n - 1)
print(v)
