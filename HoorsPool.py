def displacement(p, m, d, v):
    for i in d.keys():
        d[i] = m
    for i in range(v, v+m-1):
        d[p[i]] = m+v-1-i


def horspool(t, n, p, size, v):
    d = dict.fromkeys('abcdefghijklmnopqrstuvwxyz ')
    displacement(p, size, d, v)
    print(d)
    i = size - 1
    index = -1
    while i < n:
        k = 0
        while k < size and p[size - 1 - k + v] == t[i - k]:
            k = k + 1
        if k == size:
            index = i - size + 1
        i += d[t[i]]
    return index


def sufix(t, n, p, m):
    size = m
    index = -1
    for v in range(m):
        index = horspool(t, n, p, size, v)
        if index != -1:
            break
        size -= 1
    if index != -1:
        print(index, index+size-1)
    else:
        print("Não há")


t = 'nunca desista cultue a perseveranca'
p = 'cultue'
sufix(t, len(t), p, len(p))
