def calc_next(p, m, next):
    next[0] = -1
    if m != 1:
        next[1] = 0
    for i in range(2, m):
        j = next[i-1]
        while j >= 0 and p[i-1] != p[j]:
            j = next[j]
        next[i] = j + 1


def kmp_column(t, n, p, m):
    index = [0]*2
    index[0] = -1
    index[1] = -1
    for k in range(n):
        next = [0]*m
        calc_next(p, m, next)
        i = 0
        j = 0
        while index[0] == -1 and i < n:
            if t[i][k] == p[j]:
                j += 1
                i += 1
            else:
                j = next[j]
                if j == -1:
                    j = 0
                    i += 1
            if j == m:
                index[1] = k
                index[0] = i-m
        if index[0] != -1:
            break
    return index


def kmp_line(t, n, p, m):
    index = [0]*2
    index[0] = -1
    index[1] = -1
    for k in range(n):
        next = [0]*m
        calc_next(p, m, next)
        i = 0
        j = 0
        while index[0] == -1 and i < n:
            if t[k][i] == p[j]:
                j += 1
                i += 1
            else:
                j = next[j]
                if j == -1:
                    j = 0
                    i += 1
            if j == m:
                index[0] = k
                index[1] = i-m
        if index[0] != -1:
            break
    return index


def words_s(words, n_words, words_size, t, n):
    for i in range(n_words):
        m = words_size[i]
        index = kmp_line(t, n, words[i], m)
        if index[0] == -1:
            index = kmp_column(t, n, words[i], m)
            print(f"{words[i]}, ({index[0]}, {index[1]}), ({index[0] + m - 1}, {index[1]})")
        else:
            print(f"{words[i]}, ({index[0]}, {index[1]}), ({index[0]}, {index[1] + m - 1})")


t = [['p', 'o', 'o'],
     ['a', 'b', 'c'],
     ['a', 's', 'l']]
words = ['paa', 'obs', 'sl', 'poo']
words_size = [3, 3, 2, 3]
words_s(words, len(words), words_size, t, len(t[0]))
