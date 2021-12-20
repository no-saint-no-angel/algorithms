
t = [100, 50, 20, 5, 1]


def change(n, t):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n//money
        n -= m[i]*money
    print([m, n])
    return m, n


my_change = change(98, t)