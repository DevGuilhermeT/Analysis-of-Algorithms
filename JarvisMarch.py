def rightmost_point(v):
    rmp = 0
    for i in range(1, len(v)):
        if v[i][0] > v[rmp][0]:
            rmp = i
        elif v[i][0] == v[rmp][0]:
            if v[i][1] < v[rmp][1]:
                rmp = i
    return rmp


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def jarvis_march(v, n, depth):
    if n < 3:
        return
    l = rightmost_point(v)
    hull = [[]] * n
    pos = 0
    p = l
    q = 0
    while True:
        hull[pos] = p
        pos += 1
        q = (p + 1) % n
        for i in range(n):
            if orientation(v[p], v[i], v[q]) == 2:
                q = i
        p = q
        if p == l:
            break

    n_aux = n
    print("Depth", depth, ":")
    for x in range(pos):
        print(v[hull[x]][0], v[hull[x]][1])
        v[hull[x]] = [[]]
        n -= 1
    depth += 1
    v_aux = [[]]*n
    pos2 = 0
    for i in range(n_aux):
        if v[i] != [[]]:
            v_aux[pos2] = v[i]
            pos2 += 1
    return v_aux, n, depth


def ans(v, n, depth):
    while n > 2:
        v, n, depth = jarvis_march(v, n, depth)
    if n > 0:
        print("Depth", depth, ":")
        for x in range(n):
            print(v[x][0], v[x][1])


depth = 0
lista = [[0, 0], [10, 0], [10, 10], [0, 10], [1, 1], [1, 9], [9, 9], [9, 1], [5, 5], [4, 4]]
ans(lista, len(lista), depth)
