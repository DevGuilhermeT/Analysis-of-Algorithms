class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = None
        if self.weight is not None:
            self.ratio = self.value/self.weight


class Node:
    def __init__(self, parent=None, direction=None, level=None, profit=None, bound=None, weight=None):
        self.parent = parent
        self.direction = direction
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight


def min_heapify(v, i, n):
    p = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and v[l].ratio < v[p].ratio:
        p = l
    if r < n and v[r].ratio < v[p].ratio:
        p = r
    if p != i:
        v[i], v[p] = v[p], v[i]
        min_heapify(v, p, n)


def create_min_heap(v, n):
    last_parent = (n-2)//2
    for i in range(last_parent, -1, -1):
        min_heapify(v, i, n)


def heapsort(v, n):
    create_min_heap(v, n)
    for i in range(n-1, 0, -1):
        v[i], v[0] = v[0], v[i]
        min_heapify(v, 0, i)


def max_heapify(v, i, n):
    p = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and v[l].bound > v[p].bound:
        p = l
    if r < n and v[r].bound > v[p].bound:
        p = r
    if p != i:
        v[i], v[p] = v[p], v[i]
        max_heapify(v, p, n)


def insertion_max_heap(v, k, x):
    k += 1
    v[k - 1] = x
    son = k-1
    p = (k - 2) // 2
    while p >= 0:
        if v[p].bound < v[son].bound:
            v[p], v[son] = v[son], v[p]
            son = p
            p = (son - 1) // 2
        else:
            p = -1
    return k


def get_maximum(v, k):
    maximum = v[0]
    v[0], v[k - 1] = v[k - 1], v[0]
    k -= 1
    max_heapify(v, 0, k)
    return maximum, k


def print_result(items, ans):
    if ans.parent is not None:
        print_result(items, ans.parent)
        if ans.direction == 'l':
            print(f"[{items[ans.level].weight}, {items[ans.level].value}]")


def calculate_bound(node, items, capacity, n):
    if node.level < (n-1):
        bound = node.profit + (capacity - node.weight) * items[node.level+1].ratio
    else:
        bound = node.profit
    return bound


def knapsack(capacity, v, n):
    items = [Item(None, None)]*n
    for i in range(n):
        items[i] = Item(v[i][0], v[i][1])
    heapsort(items, n)

    queue = [[] for _ in range((2**(n+1))-1)]
    optimal_ans = Node()
    n_queue = 0

    u = Node(None, None, -1, 0, None, 0)
    v = Node()

    u.bound = capacity * items[0].ratio
    n_queue = insertion_max_heap(queue, n_queue, u)

    max_profit = 0

    while n_queue != 0:
        u, n_queue = get_maximum(queue, n_queue)

        if u.level != n-1:
            if u.bound >= max_profit:
                v.level = u.level + 1
                v.weight = u.weight + items[v.level].weight
                v.profit = u.profit + items[v.level].value
                v.parent = u

                if v.weight <= capacity and v.profit > max_profit:
                    max_profit = v.profit

                v.bound = calculate_bound(v, items, capacity, n)

                if v.bound >= max_profit and v.weight <= capacity:
                    left_node = Node(v.parent, 'l', v.level, v.profit, v.bound, v.weight)
                    n_queue = insertion_max_heap(queue, n_queue, left_node)

                right_node = Node(v.parent, 'r', v.level, u.profit, None, u.weight)
                right_node.bound = calculate_bound(right_node, items, capacity, n)

                if right_node.bound >= max_profit and right_node.weight <= capacity:
                    n_queue = insertion_max_heap(queue, n_queue, right_node)
        else:
            optimal_ans = u

    print_result(items, optimal_ans)

    return max_profit


v = [[5, 25], [7, 42], [4, 40], [3, 12]]
n = len(v)
w = 10
print(knapsack(w, v, n))