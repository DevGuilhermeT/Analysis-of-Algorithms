def possibilities_n(v, pos, target):
    if target == 0:
        return 1
    if pos < 0:
        return 0
    exclude = possibilities_n(v, pos - 1, target)
    subtract = possibilities_n(v, pos - 1, target - v[pos])
    add = possibilities_n(v, pos - 1, target + v[pos])
    return exclude + subtract + add


vec = [1, 4, -3, 3]
target = 5
print(possibilities_n(vec, len(vec) - 1, target))