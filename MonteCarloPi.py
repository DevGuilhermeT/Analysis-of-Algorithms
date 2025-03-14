from random import uniform


def pi():
    n = 100000
    count = 0
    for i in range(n):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1
    return 4 * (count/n)


print(pi())
