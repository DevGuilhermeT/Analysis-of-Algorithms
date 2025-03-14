def number_order(v, n):
    pos = n
    neg = 0
    j = 0
    while j <= pos:
        if v[j] > 0:
            v[j], v[pos] = v[pos], v[j]
            pos = pos - 1
        elif v[j] < 0:
            v[j], v[neg] = v[neg], v[j]
            neg = neg + 1
            j = j + 1
        else:
            j = j + 1

v = [-1,2,3,0,0,0,1,2,3,-1,2,-3,-4]
number_order(v, len(v)-1)
print(v)
