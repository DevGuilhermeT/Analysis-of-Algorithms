def counting_sort(a, b, n, k):
    c = [0]*(k+1)
    cont = 0
    for i in range(n):
        cont += c[a[i]]
        c[a[i]] += 1
    for i in range(1, k+1):
        c[i] += c[i-1]
    for i in range(n-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1
    return cont


v = [1, 2, 3, 2, 5, 3, 1, 0, 2]
b = [0]*len(v)
a = counting_sort(v, b, len(v), 5)
print(a)
print(b)