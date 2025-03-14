from random import randint


def escolha():
    v = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    i = randint(0, 9)
    return v[i]


def escolha_justa():
    while True:
        x1 = escolha()
        x2 = escolha()
        if x1 != x2:
            return x1


print(escolha_justa())
