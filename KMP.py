def calc_next(p, m, next):
    next[0] = -1
    if m != 1:
        next[1] = 0
    for i in range(2, m):
        j = next[i-1]
        while j >= 0 and p[i-1] != p[j]:
            j = next[j]
        next[i] = j + 1


def kmp(t, n, p, k):
    next = [0]*k
    calc_next(p, k, next)
    i = 0
    j = 0
    while i < n:
        if t[i] == p[j]:
            j += 1
            i += 1
        else:
            j = next[j]
            if j == -1:
                j = 0
                i += 1
        if j == k:
            print(i-k, end=" ")
            j = 0


t = 'Vejam as araras e ararinhas azuis na arvore durante a viagem'
p = 'ara'
k = 2
kmp(t, len(t), p, k)
