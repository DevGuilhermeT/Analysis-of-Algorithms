def build_max_heap(v, n):
    last_parent = (n-2)//2
    for i in range(last_parent, -1, -1):
        max_heapify(v, i, n)


def max_heapify(v, i, n):
    p = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and v[l][1] >= v[p][1]:
        if v[l][1] > v[p][1]:
            p = l
        elif v[l][1] == v[p][1] and v[l][2] > v[p][2]:
            p = l
    if r < n and v[r][1] >= v[p][1]:
        if v[r][1] > v[p][1]:
            p = r
        elif v[r][1] == v[p][1] and v[r][2] > v[p][2]:
            p = r
    if p != i:
        v[i], v[p] = v[p], v[i]
        max_heapify(v, p, n)


def heapsort(v, n):
    build_max_heap(v, n)
    for i in range(n-1, 0, -1):
        v[i], v[0] = v[0], v[i]
        max_heapify(v, 0, i)


def v_tuples(v):
    tuple_v = []
    cont = 0
    for number in v:
        aux_tuple = (number, len(number), cont)
        tuple_v.append(aux_tuple)
        cont += 1
    return tuple_v


def print_array(array):
    for value in array:
        print(value[0], end=" ")


string_t = ['casa', 'apocalipse', 'deveras', 'entropia', 'mesmero', 'blafemia', 'albedo', 'mefisto', 'tirania', 'absurdo']
arr = v_tuples(string_t)
heapsort(arr, len(arr))
print_array(arr)
