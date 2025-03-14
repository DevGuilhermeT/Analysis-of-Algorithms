def calc_next(p, m, next, first):
    next[0] = -1
    if m != 1:
        next[1] = first
    for i in range(2, m):
        j = next[i-1]
        while j >= 0 and p[i-1+first] != p[j+first]:
            j = next[j]
        next[i] = j + 1


def kmp(t, n, p, m, next_start, first):
    next = [0]*m
    calc_next(p, m, next, first)
    i = next_start
    j = first
    index = -1
    while index == -1 and i < n:
        if t[i] == p[j]:
            j += 1
            i += 1
        else:
            j = next[j-first]
            if j == -1:
                j = first
                i += 1
        if j == m+first:
            index = i-m
    return index


def pattern_search(t, n, p, m):
    first = 0
    count = 0
    next_start = 0
    for i in range(0, m):
        if p[i] == '#':
            if i != 0:
                index = kmp(t, n, p, count, next_start, first)
                first = i + 1
                next_start = index + count
                count = 0
                if index == -1:
                    return False
            else:
                first = 1
        elif p[i] != '#':
            count += 1
        if i == m-1 and p[i] != '#':
            index = kmp(t, n, p, count, next_start, first)
            if index == -1:
                return False
    return True


p = 'ab#ba#c#'
t = 'cabccbacbacab'
print(pattern_search(t, len(t), p, len(p)))

