def odd_even(v, i, j):
    start = i
    end = j
    while start < end:
        while start < j and v[start] % 2 == 0:
            start += 1
        while end > i and v[end] % 2 != 0:
            end -= 1
        if start < end:
            v[start], v[end] = v[end], v[start]
    p = end
    v[i], v[p] = v[p], v[i]
    return p


def partition(v, i, j, oe):
    pivot = v[i]
    start = i
    end = j
    if oe == 1:
        while start < end:
            while start <= j and v[start] <= pivot:
                start += 1
            while end >= i and v[end] > pivot:
                end -= 1
            if start < end:
                v[start], v[end] = v[end], v[start]
    else:
        while start < end:
            while start <= end and v[start] >= pivot:
                start += 1
            while end >= start and v[end] < pivot:
                end -= 1
            if start < end:
                v[start], v[end] = v[end], v[start]

    p = end
    v[i], v[p] = v[p], v[i]
    return p


def quick_sort(v, i, j, oe):
    if i < j:
        pos = partition(v, i, j, oe)
        quick_sort(v, i, pos-1, oe)
        quick_sort(v, pos+1, j, oe)


def ans(v, n):
    pos = odd_even(v, 0, n-1)
    if v[pos] % 2 != 0:
        pos = pos - 1
    quick_sort(v, 0, pos, 1)
    quick_sort(v, pos+1, n-1, 2)


vect = [5,2,9,7,3,6,4,10]
ans(vect, len(vect))
print(vect)
