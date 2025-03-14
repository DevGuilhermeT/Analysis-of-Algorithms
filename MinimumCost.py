from math import inf, factorial


class Node:
    def __init__(self, parent, worker, job, filled_jobs, fixed_cost=0, bound=0):
        self.parent = parent
        self.worker = worker
        self.job = job
        self.filled_jobs = [x for x in filled_jobs]
        self.fixed_cost = fixed_cost
        self.bound = bound
        if self.job != -1:
            self.filled_jobs[self.job] = True


def min_heapify(v, i, n):
    p = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and v[l].bound < v[p].bound:
        p = l
    if r < n and v[r].bound < v[p].bound:
        p = r
    if p != i:
        v[i], v[p] = v[p], v[i]
        min_heapify(v, p, n)


def insertion_min_heap(v, k, x):
    k += 1
    v[k - 1] = x
    son = k-1
    p = (k - 2) // 2
    while p >= 0:
        if v[p].bound > v[son].bound:
            v[p], v[son] = v[son], v[p]
            son = p
            p = (son - 1) // 2
        else:
            p = -1
    return k


def calculate_minimum_cost(matrix, x, filled, n):
    cost = 0

    for i in range(x+1, n):
        minimum = inf
        for j in range(n):
            if filled[j] is False and matrix[i][j] < minimum:
                minimum = matrix[i][j]
        cost += minimum
    return cost


def print_result(minimum):
    if minimum.parent is not None:
        print_result(minimum.parent)
        print("Pessoa: ", minimum.worker, " Tarefa: ", minimum.job)


def get_minimum(v, k):
    minimum = v[0]
    v[0], v[k - 1] = v[k - 1], v[0]
    k -= 1
    min_heapify(v, 0, k)
    return minimum, k


def minimum_cost(matrix, n):
    queue = [[]] * factorial(n)
    n_queue = 0
    filled = [[]]*n
    for i in range(n):
        filled[i] = False
    root = Node(None, -1, -1, filled)

    n_queue = insertion_min_heap(queue, n_queue, root)

    while n_queue != 0:
        minimum, n_queue = get_minimum(queue, n_queue)
        i = minimum.worker + 1
        if i == n:
            print_result(minimum)
            return minimum.bound

        for j in range(n):
            if minimum.filled_jobs[j] is False:
                son = Node(minimum, i, j, minimum.filled_jobs)
                son.fixed_cost = minimum.fixed_cost + matrix[i][j]
                son.bound = son.fixed_cost + calculate_minimum_cost(matrix, i, son.filled_jobs, n)
                n_queue = insertion_min_heap(queue, n_queue, son)


matrix = [[9, 2, 7, 8],
          [6, 4, 3, 7],
          [5, 8, 1, 8],
          [7, 6, 9, 4]]
n = len(matrix)
print(minimum_cost(matrix, n))